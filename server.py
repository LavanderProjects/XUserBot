import os
from flask import Flask
from flask_restful import Resource, Api
from config import API_ID
app = Flask(__name__)
api = Api(app)

class Greeting(Resource):
    def get(self):
        return "XUserbot Aktif Ve Çalışıyor!" + str(API_ID)

api.add_resource(Greeting, '/')

app.run(host="0.0.0.0", port=os.environ.get("PORT", 8080))
