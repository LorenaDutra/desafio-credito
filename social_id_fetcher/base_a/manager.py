import random

from sqlalchemy.orm import sessionmaker
from  sqlalchemy.sql.expression import func, select
from pycpfcnpj.gen import cpf as cpf_generator

from base_a.connection import get_engine
from base_a.models import Person, Divida
from base_a.utils import (name_generator, address_generator,
                          company_generator, value_generator,
                          status_generator, contract_generator)


PEOPLE_COUNT = 1000


class Manager(object):
    def __init__(self, *args, **kwargs):
        self.engine = get_engine()

    def drop_models_tables(self):
        Divida.__table__.drop(bind=get_engine(), checkfirst=True)
        Person.__table__.drop(bind=get_engine(), checkfirst=True)

    def create_models_tables(self):
        Person.__table__.create(bind=get_engine(), checkfirst=True)
        Divida.__table__.create(bind=get_engine(), checkfirst=True)
    
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
                name=name_generator(),
                address=person_info['address']
            )
            persons.append(person)

            for _ in range(3):
                dividas.append(Divida(
                    company=company_generator(),
                    value=value_generator(),
                    status=status_generator(),
                    contract=contract_generator(),
                    person_cpf=person.cpf
                ))
        session.add_all(persons)
        session.add_all(dividas)
        session.commit()
    
    def start_db(self):
        self.restart_models_tables()
        self.generate_people()
