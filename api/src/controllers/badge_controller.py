from flask import request
from flask_restplus import Resource

from utils.dto import BadgeDto
from services.badge_service import get_all_badges, get_a_badge

api = BadgeDto.api
_badge = BadgeDto.badge


@api.route('/')
class BadgeList(Resource):
    @api.doc('list_of_registered_badges')
    @api.marshal_list_with(_badge, envelope='data')
    def get(self):
        """List all registered badges"""
        return get_all_badges()


@api.route('/<name>')
@api.param('name', 'The Badge identifier')
@api.response(404, 'Badge not found.')
class Badge(Resource):
    @api.doc('get a badge')
    @api.marshal_with(_badge)
    def get(self, name):
        """get a badge given its identifier"""
        badge = get_a_badge(name)
        if not badge:
            api.abort(404)
        else:
            return badge