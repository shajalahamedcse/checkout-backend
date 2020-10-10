# from src.server import db
# #from src.server.models.promo_details import PromoDetails
#
#
# class Promo(db.Model):
#
#     __tablename__ = "promos"
#     id = db.Column(db.Integer, primary_key=True, autoincrement=True)
#     promo_code = db.Column(db.String(255), nullable=False, unique=True)
#     # Conditional Promo
#     is_flat = db.Column(db.Boolean, nullable=False, default=True)
#     # percentage(True) or amount(False)
#     discount_type = db.Column(db.Boolean, nullable=False, default=True)
#     amount = db.Column(db.Float, nullable=False, default=0)
#     #promo_details = db.relationship('PromoDetails', secondary='promo_relations')
#
#     def __init__(self, promo_code, is_flat, discount_type, amount):
#         self.promo_code = promo_code
#         self.is_flat = is_flat
#         self.discount_type = discount_type
#         self.amount = amount
#
#
#
#
