from flask import Blueprint, request, make_response, jsonify
from flask.views import MethodView


home_blueprint = Blueprint('books', __name__)


class GetHomeApi(MethodView):

    def get(self):
        response_object = {
            'message': "Server is running"
        }
        return make_response(jsonify(response_object)), 200


home_view = GetHomeApi.as_view('home_api')

home_blueprint.add_url_rule(
    '/api/v1/home',
    view_func=home_view,
    methods=['GET']
)