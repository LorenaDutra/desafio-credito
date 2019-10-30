import sys
import csv

sys.path.insert(0, './social_id_fetcher')
sys.path.insert(0, './score_calculator')
sys.path.insert(0, './social_trail_fetcher')

from pycpfcnpj.gen import cpf as cpf_generator

from base_a.manager import Manager as ManagerA
from base_a.utils import address_generator
from base_b.manager import Manager as ManagerB
from base_c.manager import Manager as ManagerC


PEOPLE_COUNT = 1000

def generate_data():
    id_list = []
    for _ in range(PEOPLE_COUNT):
        id_list.append({
            'cpf': cpf_generator(),
            'address': address_generator()
        })

    print('Gerando dados para Base A')
    manager_a = ManagerA()
    manager_a.restart_models_tables()
    manager_a.generate_people(id_list)

    print('Gerando dados para Base B')
    manager_b = ManagerB()
    manager_b.restart_models_tables()
    manager_b.generate_people(id_list)

    print('Gerando dados para Base C')
    manager_c = ManagerC()
    manager_c.drop_collection()
    manager_c.generate_people(id_list)

    with open('people.csv', 'w', newline='') as csvfile:
        peoplewriter = csv.writer(csvfile, delimiter=' ',
                                quotechar='|', quoting=csv.QUOTE_MINIMAL)
        peoplewriter.writerow(['csv', 'address'])
        for person_info in id_list:
            peoplewriter.writerow(person_info.values())

if __name__ == "__main__":
    # execute only if run as a script
    generate_data()