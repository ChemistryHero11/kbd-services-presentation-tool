from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import uuid

db = SQLAlchemy()

# Junction table for many-to-many relationship between presentations and products
presentation_products = db.Table('presentation_products',
    db.Column('presentation_id', db.Integer, db.ForeignKey('presentation.id'), primary_key=True),
    db.Column('product_id', db.Integer, db.ForeignKey('product.id'), primary_key=True)
)

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    category = db.Column(db.String(50), nullable=False)
    collection = db.Column(db.String(50))
    item_name = db.Column(db.String(100), nullable=False)
    dimensions = db.Column(db.String(50))
    price = db.Column(db.String(20))
    notes = db.Column(db.Text)
    
    # Relationship to product codes
    product_codes = db.relationship('ProductCode', backref='product', lazy=True)

    def __repr__(self):
        return f"<Product {self.id}: {self.item_name}>"

class ProductCode(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(20), nullable=False)
    color = db.Column(db.String(30))
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)

    def __repr__(self):
        return f"<ProductCode {self.code} - {self.color}>"

class Presentation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    client_name = db.Column(db.String(100))
    company_name = db.Column(db.String(100))
    budget = db.Column(db.String(50))
    purpose = db.Column(db.String(50))
    timeline = db.Column(db.String(50))
    created_date = db.Column(db.DateTime, default=datetime.utcnow)
    unique_link = db.Column(db.String(50), unique=True)
    
    # Relationship to selected products
    products = db.relationship('Product', secondary=presentation_products, backref=db.backref('presentations', lazy='dynamic'))

    def __repr__(self):
        return f"<Presentation {self.id} for {self.client_name}>"
    
    @staticmethod
    def generate_unique_link():
        """Generate a random 8-character unique link"""
        return str(uuid.uuid4())[:8]
