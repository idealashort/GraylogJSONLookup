from flask import Flask
from flask_restful import Api, Resource
import json

app = Flask(__name__)
api = Api(app)
clients = {}


class Client(Resource):
    def get(self, client_name):
        with open('client.json') as clients_file:
            clients = json.load(clients_file)
        return clients[client_name.upper()]


api.add_resource(Client, "/client/<string:client_name>")

if __name__ == '__main__':
    app.run(debug=True)
