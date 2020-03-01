from flask_restplus import Api
from flask import Blueprint

from controllers.user_controller import api as user_ns
from controllers.badge_controller import api as badge_ns

blueprint = Blueprint('api', __name__)

api = Api(blueprint,
            version='0.1',
            title='Gitlab RS',
            description='A web interface allowing your team to visualize their GitLab statistics.'
        )

api.add_namespace(user_ns, path='/user')
api.add_namespace(badge_ns, path='/badge')