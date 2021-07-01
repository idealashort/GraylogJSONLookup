import json


def add_client(name, windows_security, windows_event, palo):
    new_client = {
        "client": {
            "name": name,
            "streams": {
                "windows_security": windows_security,
                "windows_event": windows_event,
                "palo": palo
            }
        }
    }
    with open('client.json', "r+") as c:
        clients = json.load(c)
        clients.append(new_client)
        c.seek(0)
        json.dump(clients, c)
        c.truncate()
    return new_client