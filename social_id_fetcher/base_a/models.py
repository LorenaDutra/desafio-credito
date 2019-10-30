from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.types import ARRAY


Base = declarative_base()


class Person(Base):
    __tablename__ = 'person'

    cpf = Column(String, primary_key=True)
    name = Column(String)
    address = Column(String)
    dividas = relationship("Divida", lazy='subquery')

    def __repr__(self):
        return f'<Person(cpf={self.cpf}, name={self.name})>'


class Divida(Base):
    __tablename__ = 'divida'

    id = Column(Integer, primary_key=True)
    company = Column(String)
    value = Column(Integer)
    status = Column(String)
    contract = Column(Integer)

    person_cpf = Column(String, ForeignKey('person.cpf'))

    def __repr__(self):
        return f'<Divida(company={self.company}, value={self.value})>'
