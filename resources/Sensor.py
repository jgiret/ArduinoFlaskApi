# -*- coding: utf-8 -*-
# @Author: Jean-Christophe Giret
# @Date:   2018-01-08 22:05:04
# @Last Modified by:   Jean-Christophe Giret
# @Last Modified time: 2018-01-08 22:33:36

from flask import request
from flask_restful import Resource
from db.Sqlite import session
from models.OregonData import OregonData


class Sensor(Resource):

    """Class Sensor
    """

    def get(self):
        """GET method

        Returns:
            array:Return an array of OregonData object
        """
        data = session.query(OregonData).all()
        data_dict = [d.as_dict() for d in data]
        return data_dict

    def post(self):
        """POST method

        Returns:
            [OregonData]: Description
        """
        if request.json:
            mydata = request.json

            data1 = OregonData(device=mydata["device"], deviceId=int(mydata["deviceId"]),
                               temperature=float(mydata["temperature"]), humidity=float(mydata["humidity"]))
            session.add(data1)
            session.commit()

            return True

        else:
            return False
