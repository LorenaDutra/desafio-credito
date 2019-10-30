from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.types import ARRAY


Base = declarative_base()


class Person(Base):
    __tablename__ = 'person'

    cpf = Column(String(12), primary_key=True)
    age = Column(Integer)
    address = Column(String(50))
    assets = relationship("Asset", lazy='subquery')
    
    def __repr__(self):
        return f'<Person(cpf={self.cpf}, name={self.name})>'


class Asset(Base):
    __tablename__ = 'asset'

    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    value = Column(Integer)

    person_cpf = Column(String(12), ForeignKey('person.cpf'))

    def __repr__(self):
        return f'<Asset(company={self.company}, value={self.value})>'
