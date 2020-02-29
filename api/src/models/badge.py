from flask_restplus import fields
from server.instance import server

badge = server.api.model('Badge', {
    'id': fields.Integer(description='Id'),
    'title': fields.String(required=True, min_length=1, max_length=64, description='Badge name'),
    'description': fields.String(max_length=256, description='Badge description'),
    'image': fields.String(description="Badge image URI"),
    'created_at': fields.DateTime(required=True, description="Badge creation date")
})