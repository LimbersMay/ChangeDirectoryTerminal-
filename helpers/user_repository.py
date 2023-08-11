import json
from io import open


class UserRepository:
    def __init__(self, path):
        self.path = path

    def save(self, key, value):
        with open(self.path, "r") as file:
            json_data = json.loads(file.read())

        json_data[key] = value

        with open(self.path, "w") as file:
            file.write(json.dumps(json_data, indent=4))

    def find_one(self, key):
        with open(self.path, "r") as file:
            json_data = json.loads(file.read())

        return json_data[key]

    def find_all(self):
        with open(self.path, "r") as file:
            json_data = json.loads(file.read())

        return json_data

    def delete(self, key):
        with open(self.path, "r") as file:
            json_data = json.loads(file.read())

        del json_data[key]

        with open(self.path, "w") as file:
            file.write(json.dumps(json_data, indent=4))