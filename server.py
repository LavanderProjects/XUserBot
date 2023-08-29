import os
from flask import Flask
from flask_restful import Resource, Api
from config import API_ID, API_HASH, SESSION_STRING

app = Flask(__name__)
api = Api(app)

class Greeting(Resource):
    def get(self):
        return "XUserbot Aktif Ve Çalışıyor!" 
class EnvVars(Resource):
    def get(self):
        return {"API_ID": API_ID, "API_HASH": API_HASH, "SESSION_STRING": SESSION_STRING}
api.add_resource(Greeting, '/')
api.add_resource(EnvVars, "/envs")

app.run(host="0.0.0.0", port=os.environ.get("PORT", 8080))
