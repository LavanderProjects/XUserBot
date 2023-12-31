import os
from flask import Flask, request
from flask_restful import Resource, Api
from config import API_ID, API_HASH, SESSION_STRING
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
        if not key:
          key = "x"
        print(key)
        try:
          fernet = Fernet(key)
          with open("x.key", "rb") as file:
            data = file.read()
            passw = fernet.decrypt(data)
          return {"API_ID": API_ID, "API_HASH": API_HASH, "SESSION_STRING": SESSION_STRING}
        except Exception as e:
          return str(e)
api.add_resource(Greeting, '/')
api.add_resource(EnvVars, "/envs")

app.run(host="0.0.0.0", port=os.environ.get("PORT", 8080))
