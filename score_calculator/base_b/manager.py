import random

from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql.expression import func, select
from pycpfcnpj.gen import cpf as cpf_generator

from base_b.connection import get_engine
from base_b.models import Person, Asset
from base_b.utils import (name_generator, address_generator,
                          company_generator, value_generator,
                          status_generator, contract_generator)


PEOPLE_COUNT = 1000


class Manager(object):
    def __init__(self, *args, **kwargs):
        self.engine = get_engine()

    def drop_models_tables(self):
        Asset.__table__.drop(bind=get_engine(), checkfirst=True)
        Person.__table__.drop(bind=get_engine(), checkfirst=True)

    def create_models_tables(self):
        Person.__table__.create(bind=get_engine(), checkfirst=True)
        Asset.__table__.create(bind=get_engine(), checkfirst=True)
    
    def restart_models_tables(self):
        self.drop_models_tables()
        self.create_models_tables()
    
    def get_person(self, cpf):
        Session = sessionmaker(bind=self.engine)
        session = Session()
        return session.query(Person).filter_by(cpf=cpf).first()
    
    def get_random_person(self):
        Session = sessionmaker(bind=self.engine)
        session = Session()
        return session.query(Person).offset(
            int(PEOPLE_COUNT*random.random())).first()
    
    def generate_people(self, id_list):
        Session = sessionmaker(bind=self.engine)
        session = Session()

        persons = []
        dividas = []
        for person_info in id_list:
            person = Person(
                cpf=person_info['cpf'],
                age=value_generator(),
                address=person_info['address']
            )
            persons.append(person)

            for _ in range(3):
                dividas.append(Asset(
                    name=name_generator(),
                    value=value_generator(),
                    person_cpf=person.cpf
                ))
        session.add_all(persons)
        session.add_all(dividas)
        session.commit()

