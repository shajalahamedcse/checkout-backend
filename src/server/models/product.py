from src.server import db


class Product(db.Model):
    __tablename__ = "products"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    product_id = db.Column(db.String(255), unique=True, nullable=False)
    product_name = db.Column(db.String(255), nullable=False)
    price = db.Column(db.Float, nullable=False)
    #promo_details = db.relationship('PromoDetails', secondary='product_promo')

    def __init__(self, product_id, product_name, price):
        self.product_id = product_id
        self.product_name = product_name
        self.price = price

    def __repr__(self):
        return '<Product: id: {}'.format(self.product_id)


class Promo(db.Model):

    __tablename__ = "promos"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    promo_code = db.Column(db.String(255), nullable=False, unique=True)
    # Conditional Promo
    is_flat = db.Column(db.Boolean, nullable=False, default=True)
    # percentage(True) or amount(False)
    discount_type = db.Column(db.Boolean, nullable=False, default=True)
    amount = db.Column(db.Float, nullable=False, default=0)
    least_amount = db.Column(db.Float, nullable=False, default=0)
    valid = db.Column(db.Boolean, nullable=False, default=True)
    #promo_details = db.relationship('PromoDetails', secondary='promo_relations')

    def __init__(self, promo_code, is_flat, discount_type, amount, least_amount):
        self.promo_code = promo_code
        self.is_flat = is_flat
        self.discount_type = discount_type
        self.amount = amount
        self.least_amount = least_amount


class PromoDetails(db.Model):
    __tablename__ = 'promo_details'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    promo_id = db.Column(db.Integer, db.ForeignKey('promos.id'))
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'))
    quantity = db.Column(db.Integer, nullable=False)
    target_product_id = db.Column(db.Integer, nullable=False)

    def __init__(self, promo_id, product_id, quantity, target_product_id):
        self.promo_id = promo_id
        self.product_id = product_id
        self.quantity = quantity
        self.target_product_id = target_product_id
