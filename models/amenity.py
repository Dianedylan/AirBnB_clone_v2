#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class Amenity(BaseModel, Base):
    """Amenity class to store amenities of each place"""
    __tablename__ = 'amenities'
    name = Column(String(128), nullable=False)
    place_amenities = relationship('Review',
                                   secondary='place_amenity',
                                   backref='amenity')

    def __init__(self, *args, **kwargs):
        self.name = kwargs['name']
        super().__init__(*args)
