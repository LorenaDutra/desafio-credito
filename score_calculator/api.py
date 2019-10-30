from flask import Flask, abort
from flask_restful import Resource, Api

from base_b.manager import Manager
from score import calculate_score

app = Flask(__name__)
api = Api(app)

class Person(Resource):
    def get(self, cpf):
        manager = Manager()
        person = manager.get_person(cpf)
        
        if person:
            payload = {
                'cpf': person.cpf,
                'score': calculate_score(person),
                'age': person.age,
                'address': person.address,
                'assets': [{
                    'name': asset.name,
                    'value': asset.value
                } for asset in person.assets]
            }
            return payload
        else:
            abort(400)

api.add_resource(Person, '/score/<string:cpf>')

if __name__ == '__main__':
    app.run(debug=True)
