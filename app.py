#!flask/bin/python

from flask import Flask
from flask_restful import Api


from resources.Sensor import Sensor
from resources.Hello import Hello


app = Flask(__name__)
api = Api(app)

api.add_resource(Hello, '/')
api.add_resource(Sensor, '/sensor')

if __name__ == '__main__':
    app.run(debug=True)
