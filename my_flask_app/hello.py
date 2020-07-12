from flask import Flask
from flask_restful import Api, Resource, reqparse

app = Flask(__name__)
api = Api(app)

users = [
    {
        "name": "bob",
        "age": 22,
        "password": "hello"
    },
    {
        "name": "Jane",
        "age": 25,
        "password": "password"
    }

]


class User(Resource):
    def get(self, name):
        for user in users:
            if name == user["name"]:
                return user, 200
        return "User not found", 404

    def post(self, name):
        parser = reqparse.RequestParser()
        parser.add_argument("age")
        parser.add_argument("password")
        args = parser.parse_args()

        for user in users:
            if name == user["name"]:
                return "User with the name {} already exist".format(name), 400
        user = {
            "name": name,
            "age": args["age"],
            "password": args["password"]
        }
        users.append(user)
        return user, 201

    def put(self, name):
        parser = reqparse.RequestParser()
        parser.add_argument("age")
        parser.add_argument("password")
        args = parser.parse_args()

        for user in users:
            if name == user["name"]:
                return "User with the name {} already exist".format(name), 400
        user = {
            "name": name,
            "age": args["age"],
            "password": args["password"]
        }
        users.append(user)
        return user, 201

    def delete(self, name):
        global users
        users = [user for user in users if user["name"] != name]
        return "{} is deleted.".format(name), 200


api.add_resource(User, "/user/<string:name>")

app.run(debug=True)
