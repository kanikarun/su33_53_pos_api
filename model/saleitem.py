from app import db

class SaleItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    sale_id = db.Column(db.Integer, nullable=False)    # just store ID
    product_id = db.Column(db.Integer, nullable=False) # just store ID
    qty = db.Column(db.Integer, nullable=False)
    cost = db.Column(db.Numeric(10, 2), nullable=False)
    price = db.Column(db.Numeric(10, 2), nullable=False)