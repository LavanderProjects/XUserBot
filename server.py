import os
from flask import Flask
from flask_restful import Resource, Api
from config import API_ID, API_HASH, SESSION_STRING
from flask import request
from cryptography.fernet import Fernet

# Fernet anahtarını oluşturun

app = Flask(__name__)
api = Api(app)

class Greeting(Resource):
    def get(self):
        return "XUserbot Aktif Ve Çalışıyor!"
class EnvVars(Resource):
    def get(self):
        key = request.args.get("key")
        fernet = Fernet(key)
        try:
          with open("x.key", "rb") as file:
            data = file.read().encode()
            passw = fernet.decrypt(data)
          return {"API_ID": API_ID, "API_HASH": API_HASH, "SESSION_STRING": SESSION_STRING}
        except:
          return {}
api.add_resource(Greeting, '/')
api.add_resource(EnvVars, "/envs")

app.run(host="0.0.0.0", port=os.environ.get("PORT", 8080))
