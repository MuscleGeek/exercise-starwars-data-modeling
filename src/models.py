import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Boolean, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

# class Person(Base):
#     __tablename__ = 'person'
#     # Here we define columns for the table person
#     # Notice that each column is also a normal Python instance attribute.
#     id = Column(Integer, primary_key=True)
#     name = Column(String(250), nullable=False)

# class Address(Base):
#     __tablename__ = 'address'
#     # Here we define columns for the table address.
#     # Notice that each column is also a normal Python instance attribute.
#     id = Column(Integer, primary_key=True)
#     street_name = Column(String(250))
#     street_number = Column(String(250))
#     post_code = Column(String(250), nullable=False)
#     person_id = Column(Integer, ForeignKey('person.id'))
#     person = relationship(Person)

class User(Base):
    __tablename__ = 'user'
    id= Column(Integer, primary_key=True)
    name= Column(String(50), nullable=False)
    gender = Column(String(10), nullable=False)
    password = Column(String(20), nullable=False)
    email = Column(String(50), nullable=False)

class Favorites(Base):
    __tablename__ = 'favorites'
    id= Column(Integer, primary_key=True)
    name= Column(String(50), nullable=False)
    type= Column(Boolean)
    user_id = Column(Integer, ForeignKey('user.id'))
    favorites = relationship(User)

class Planet(Base):
    __tablename__ = 'planet'
    id= Column(Integer, primary_key=True)
    name= Column(String(50), nullable=False)
    hair_color = Column(String(20), nullable=False)
    skin_color = Column(String(20), nullable=False)
    height = Column(Float, nullable=False)

class People(Base):
    __tablename__ = 'people'
    id= Column(Integer, primary_key=True)
    name= Column(String(50), nullable=False)
    diameter= Column(Float, nullable=False)
    climate= Column(String(20), nullable=False)
    terrain= Column(String(20), nullable=False)
    population= Column(Integer, nullable=False)

def to_dict(self):
    return {}
## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')