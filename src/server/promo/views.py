from flask import Blueprint, request, make_response, jsonify
from flask.views import MethodView
from src.server import db, app
from src.server.models.product import PromoDetails, Promo

promo_blueprint = Blueprint('promos', __name__)


class InsertPromoAPI(MethodView):
    def post(self):

        validation_dic = {
            'promo_code': 'promo code must be non-empty',
            'is_flat': 'is_flat must be non-empty',
            'discount_type': 'discount_type must be non-empty',
            'amount': 'amount must be non-empty',
            'quantity': 'quantity must be non-empty',
            'product_id': 'product_id must be non-empty'
        }
        response_msg = []

        promo_code = request.json.get('promo_code', None)
        is_flat = request.json.get('is_flat', None)
        discount_type = request.json.get('discount_type', None)
        amount = request.json.get('amount', None)
        target_product_id = request.json.get('target_product_id', None)

        least_amount=0
        if not is_flat:
            quantity = request.json.get('quantity', None)
            product_id = request.json.get('product_id', None)
        else:
            least_amount = request.json.get('least_amount', None)

        # if not product_id:
        #     response_msg.append(validation_dic['product_id'])
        # if not product_name:
        #     response_msg.append(validation_dic['product_name'])
        # if not price:
        #     response_msg.append(validation_dic['price'])
        try:
            promo_obj = Promo(promo_code, is_flat, discount_type, amount, least_amount)
            db.session.add(promo_obj)
            db.session.flush()
            if not is_flat and promo_obj.id:
                promo_details_obj = PromoDetails(promo_obj.id, product_id, quantity, target_product_id)
                db.session.add(promo_details_obj)
            db.session.commit()
            response_object = {
                'status': 'success',
                'message': promo_obj.promo_code + ' has been added to the promo list.'
            }
            return make_response(jsonify(response_object)), 201
        except Exception as e:
            app.logger.debug(e)
            db.session.rollback()
            response_object = {
                'status': 'fail',
                'message': 'Sorry. The action has failed because of duplicate entry. Please try again.'
            }
            return make_response(jsonify(response_object)), 400


class ApplyPromoAPI(MethodView):
    def post(self):
        promo_code = request.json.get('promo_code', None)
        cart = request.json.get('cart', None)
        subtotal = request.json.get('subtotal', None)

        try:
            promo_obj = Promo.query.filter_by(promo_code=promo_code).first()
            if promo_obj:
                if promo_obj.valid:
                    if len(cart):
                        if promo_obj.is_flat:
                            if promo_obj.discount_type and subtotal > promo_obj.least_amount: # percent
                                subtotal = subtotal - (promo_obj.amount*subtotal)/100
                            elif not promo_obj.discount_type and subtotal > promo_obj.least_amount:
                                subtotal = subtotal - promo_obj.amount
                        else:
                            promo_details_obj = PromoDetails.query.filter_by(promo_id=promo_obj.id).first()
                            if promo_details_obj:
                                for item in cart:
                                    if item["product_id"] == promo_details_obj.product_id:
                                        if item["quantity"] >= promo_details_obj.quantity:
                                            subtotal -= item["quantity"]*item["unit_price"]
                                            subtotal += item["quantity"]*promo_obj.amount
                                print(subtotal)

            response_object = {
                'validity': promo_obj.valid,
                'subtotal': subtotal
            }
            return make_response(jsonify(response_object)), 200

        except Exception as e:
            app.logger.debug(e)
            response_object = {
                'status': 'fail',
                'message': 'You are not eligible for promo'
            }
            return make_response(jsonify(response_object)), 400





add_promo_view = InsertPromoAPI.as_view('add_promo_api')
apply_promo_view = ApplyPromoAPI.as_view('apply_promo_api')

promo_blueprint.add_url_rule(
    '/api/v1/add-promo',
    view_func=add_promo_view,
    methods=['POST']
)

promo_blueprint.add_url_rule(
    '/api/v1/apply-promo',
    view_func=apply_promo_view,
    methods=['POST']
)
