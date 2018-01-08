# -*- coding: utf-8 -*-
# @Author: Jean-Christophe Giret
# @Date:   2018-01-08 22:05:09
# @Last Modified by:   Jean-Christophe Giret
# @Last Modified time: 2018-01-08 22:27:23

from flask_restful import Resource


class Hello(Resource):

    """Home class. Just a Hello World Getter
    """

    def get(self):
        """Summary

        Returns:
            str: Return Hello world!
        """
        return "Hello world!\n"
