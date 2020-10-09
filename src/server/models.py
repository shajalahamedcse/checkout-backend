from src.server import db


class Product(db.Model):
    __tablename__ = "products"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    product_id = db.Column(db.String(255), unique=True, nullable=False)
    product_name = db.Column(db.String(255), nullable=False)
    price = db.Column(db.String(255), nullable=False)

    def __init__(self, product_id, product_name, price):
        self.product_id = product_id
        self.product_name = product_name
        self.price = price

    def __repr__(self):
        return '<Product: id: {}'.format(self.product_id)
