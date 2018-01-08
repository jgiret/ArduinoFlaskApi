# -*- coding: utf-8 -*-
# @Author: Jean-Christophe Giret
# @Date:   2018-01-08 21:55:10
# @Last Modified by:   Jean-Christophe Giret
# @Last Modified time: 2018-01-08 22:01:20
#
#

from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()


class OregonData(Base):
    """OregonData model: store data sample from the THGR810 sent by the Arduino controller

    Attributes:
        device (str): Device Name
        deviceId (int): Device id
        humidity (float): Humidity (between 0 and 100)
        id (int): Primary key
        temperature (float): Temperature
    """

    __tablename__ = 'OregonData'

    id = Column(Integer, primary_key=True)
    device = Column(String)
    deviceId = Column(Integer)
    temperature = Column(Float)
    humidity = Column(Float)

    def as_dict(self):
        """Summary

        Returns:
            TYPE: Description
        """
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

    def __repr__(self):
        """Human representation of the OregonData Entry

        Returns:
            str: Sample representation
        """
        return "<Data(device='%s', deviceId='%s', temperature='%s', humidity='%s')>" % (self.device, self.deviceId, self.temperature, self.humidity)
