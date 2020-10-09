from flask import Blueprint, request, make_response, jsonify
from flask.views import MethodView
from src.server import db, app
from src.server.models import Product

product_blueprint = Blueprint('products', __name__)


class GetProductListAPI(MethodView):
    def get(self):
        pass


class AddProductAPI(MethodView):

    def post(self):
        validation_dic = {
            'product_id': 'products id must be non-empty',
            'product_name': 'products name must be non-empty',
            'price': 'price must be non-empty'
        }
        response_msg = []
        product_id = request.json.get('product_id', None)
        product_name = request.json.get('product_name', None)
        price = request.json.get('price', None)

        if not product_id:
            response_msg.append(validation_dic['product_id'])
        if not product_name:
            response_msg.append(validation_dic['product_name'])
        if not price:
            response_msg.append(validation_dic['price'])

        if len(response_msg) > 0:
            response_object = {
                'status': 'failed',
                'message': response_msg
            }
            return make_response(jsonify(response_object)), 400

        try:
            product_obj = Product(product_id, product_name, price)
            print(product_obj)
            db.session.add(product_obj)
            db.session.commit()

            response_object = {
                'status': 'success',
                'message': product_obj.product_id + ' has been added to the products list.'
            }
            return make_response(jsonify(response_object)), 201
        except Exception as e:
            app.logger.debug(e)
            response_object = {
                'status': 'fail',
                'message': 'Sorry. The action has failed because of duplicate entry. Please try again.'
            }
            return make_response(jsonify(response_object)), 400


add_product_view = AddProductAPI.as_view('add_product_api')

product_blueprint.add_url_rule(
    '/api/v1/products/add',
    view_func=add_product_view,
    methods=['POST']
)

