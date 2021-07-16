#!/usr/bin/python3
from flask import Flask
from flask_restful import Api, Resource, reqparse
import json
from addclient import add_client

app = Flask(__name__)
api = Api(app)
client_put_args = reqparse.RequestParser()
client_put_args.add_argument("windows_security", type=str,
                             help="Stream ID of the Client's Windows Security Events Stream", required=True)
client_put_args.add_argument("windows_event", type=str, help="Stream ID of the Client's Windows Events Stream",
                             required=True)
client_put_args.add_argument("palo", type=str, help="Stream ID of the Client's Palo Alto Stream")
client_put_args.add_argument("node_id", type=str, help="The ID of the client forwarder", required=True)


class Node(Resource):
    def get(self, node_id):
        with open('client.json') as clients_file:
            clients = json.load(clients_file)
        try:
            return next(filter(lambda x: x['client']['node_id'] == node_id.upper(), clients))
        except StopIteration:
            return dict(), 404

    def put(self, client_name):
        args = client_put_args.parse_args()
        return add_client(name=client_name, **args)


class Client(Resource):
    def get(self, client_name):
        with open('client.json') as clients_file:
            clients = json.load(clients_file)
        try:
            return next(filter(lambda x: x['client']['name'] == client_name.upper(), clients))
        except StopIteration:
            return dict(), 404


api.add_resource(Node, "/client/<string:node_id>")
api.add_resource(Client, "/client/name/<string:client_name>")

if __name__ == '__main__':
    app.run(debug=True)
