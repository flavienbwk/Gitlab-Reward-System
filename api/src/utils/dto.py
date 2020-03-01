from flask_restplus import Namespace, fields

class UserDto:
    api = Namespace('user', description='user related operations')
    user = api.model('User', {
        'username': fields.String(required=True, description='user username'),
        'password': fields.String(required=True, description='user password'),
        'gitlab_id': fields.String(description='user Identifier')
    })

class BadgeDto:
    api = Namespace('badge', description='badge related operations')
    badge = api.model('Badge', {
        'id': fields.Integer(description='Id'),
        'name': fields.String(required=True, min_length=1, max_length=64, description='Badge name'),
        'description': fields.String(max_length=256, description='Badge description'),
        'image': fields.String(description="Badge image URI")
    })