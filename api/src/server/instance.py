import os
from flask import Flask
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from server.create_app import create_app, database

from server.blueprint import blueprint


class Server(object):
    def __init__(self):
        self.app = create_app(os.environ.get("FLASK_ENV"))
        self.app.register_blueprint(blueprint)
        self.app.app_context().push()
        self.manager = Manager(self.app)
        migrate = Migrate(self.app, database)
        self.manager.add_command('database', MigrateCommand)
        database.init_app(self.app)

    def run(self):
        self.manager.run()

server = Server()