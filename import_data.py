import json
import os
from app import db, create_app
from models import Product, ProductCode

def import_products_from_json():
    """Import products from JSON file into SQLite database"""
    # Create application context
    app = create_app()
    with app.app_context():
        # Check if products already exist
        if Product.query.first() is not None:
            print("Products already exist in the database. Skipping import.")
            return
        
        # Load products from JSON file
        json_path = os.path.join('data', 'products.json')
        try:
            with open(json_path, 'r') as f:
                data = json.load(f)
        except FileNotFoundError:
            print(f"Error: {json_path} not found.")
            return
        except json.JSONDecodeError:
            print(f"Error: {json_path} is not valid JSON.")
            return
        
        # Import products and product codes
        print(f"Importing {len(data['products'])} products...")
        for product_data in data['products']:
            # Create product
            product = Product(
                id=product_data['id'],
                category=product_data['category'],
                collection=product_data.get('collection', ''),
                item_name=product_data['item_name'],
                dimensions=product_data.get('dimensions', ''),
                price=product_data.get('price', ''),
                notes=product_data.get('notes', '')
            )
            db.session.add(product)
            
            # Create product codes
            for code_data in product_data.get('product_codes', []):
                code = ProductCode(
                    code=code_data['code'],
                    color=code_data.get('color', ''),
                    product_id=product.id
                )
                db.session.add(code)
        
        # Commit all changes to database
        db.session.commit()
        print("Import completed successfully!")

if __name__ == '__main__':
    import_products_from_json()
