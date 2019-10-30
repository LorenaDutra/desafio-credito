import json

from flask import Flask, abort
from flask_restful import Resource, Api

from base_c.manager import Manager
from base_c.utils import person_trail_serializer

app = Flask(__name__)
api = Api(app)

class Person(Resource):
    def get(self, cpf):
        manager = Manager()
        person_trail = manager.get_person(cpf)

        if person_trail:
            return person_trail_serializer(person_trail)
        else:
            abort(400)

api.add_resource(Person, '/trail/<string:cpf>')

if __name__ == '__main__':
    app.run(debug=True)