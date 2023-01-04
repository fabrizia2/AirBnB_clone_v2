#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from models.place import Place


class City(BaseModel, Base):
    """ The city class, contains state ID and name """
    __tablename__ = "cities"
    state_id = Column(String(60), nulllable=False, ForeignKey('states.id'))
    name = Column(String(128), nullabble=False)
     places = relationship("Place", cascade='all, delete, delete-orphan', backref="cities")
