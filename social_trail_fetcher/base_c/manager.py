import random

from sqlalchemy.orm import sessionmaker
from  sqlalchemy.sql.expression import func, select
from pycpfcnpj.gen import cpf as cpf_generator

from base_c.connection import get_connection
from base_c.models import PersonTrail, Transaction, LastPurchase
from base_c.utils import (name_generator, address_generator,
                          company_generator, value_generator,
                          status_generator, contract_generator,
                          date_generator)


class Manager(object):
    def __init__(self, *args, **kwargs):
        get_connection()

    def drop_collection(self):
        PersonTrail.objects.all().delete()

    def get_person(self, cpf):
        return PersonTrail.objects.raw({'_id':cpf}).first()
    
    def get_random_person(self):
        return PersonTrail.objects.all()[
            random.randint(0, PersonTrail.objects.count() - 1)]
    
    def generate_people(self, id_list):
        for person_info in id_list:
            last_purchase = LastPurchase(
                company=company_generator(),
                date=date_generator(),
                value=value_generator()
            )

            transactions = []
            for _ in range(3):
                transactions.append(Transaction(
                    date=date_generator(),
                    value=value_generator()
                ))

            PersonTrail(
                cpf=person_info['cpf'],
                last_query=date_generator(),
                transactions=transactions,
                last_purchase=last_purchase
            ).save()
