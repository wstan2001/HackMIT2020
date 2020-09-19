from flask import Flask #, request
from flask_restful import reqparse, Api, Resource

## set up flask

app = Flask(__name__)
api = Api(app)

parser = reqparse.RequestParser()


## create a resource
class Something(Resource):
    def get(self):
        return {"nihao": "HelloWorld"}

api.add_resource(Something, '/something')