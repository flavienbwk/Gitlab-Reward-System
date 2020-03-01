from flask_restplus import fields
from server.instance import database

class Badge(database.Model):
    """ Badge Model for storing badge related details """
    __tablename__ = "badge"

    id = database.Column(database.Integer, primary_key=True, autoincrement=True)
    name = database.Column(database.String(64), unique=True, nullable=False)
    description = database.Column(database.String(255), nullable=True)
    image = database.Column(database.String(255), nullable=True)
    created_at = database.Column(database.DateTime, nullable=False)