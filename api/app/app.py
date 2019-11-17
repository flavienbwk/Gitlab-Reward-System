from flask import Flask, render_template
from flask_restplus import Api, Resource
from dotenv import load_dotenv
import socket
import os

dotenv_path = os.path.abspath('.env')
load_dotenv(dotenv_path)

app = Flask(__name__)

api = Api(app=app, version='0.1', title='Gitlab RS', description='', validate=True)

if __name__ == "__main__":
    app.run(
        debug=True,
        host='0.0.0.0', 
        port=8080
    )
