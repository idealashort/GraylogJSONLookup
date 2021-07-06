import json


def add_client(name, windows_security, windows_event, palo, node_id):
    new_client = {
        "client": {
            "name": name.upper(),
            "node_id": node_id,
            "streams": {
                "windows_security": windows_security,
                "windows_event": windows_event,
                "palo": palo
            }
        }
    }
    with open('client.json', "r+") as c:
        clients = json.load(c)
        if next(filter(lambda x: x['client']['name'] == name.upper(), clients), None):
            return {"message": "This client already exists"}
        clients.append(new_client)
        c.seek(0)
        json.dump(clients, c)
        c.truncate()
    return new_client
