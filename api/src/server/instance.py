from flask import Flask
from flask_restplus import Api, Resource, fields
from environment.instance import environment_config

class Server(object):
    def __init__(self):
        self.app = Flask(__name__)
        self.api = Api(
            self.app, 
            version='0.1',
            title='Gitlab RS',
            description='A web interface allowing your team to visualize their GitLab statistics.',
            doc=environment_config["swagger-url"]
        )

    def run(self):
        self.app.run(
                host="0.0.0.0",
                debug=environment_config["debug"], 
                port=environment_config["port"]
            )

server = Server()