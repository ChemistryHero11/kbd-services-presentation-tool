import json
import os
import sys
from app import create_app
from models import db, Product, ProductCode

def import_products_from_json():
    """Import products from JSON file into SQLite database"""
    
    print("Starting product import...")
    
    # Create application context
    app = create_app()
    with app.app_context():
        # Check if products already exist
        existing_count = Product.query.count()
        if existing_count > 0:
            print(f"{existing_count} products already exist in the database. Skipping import.")
            return
        
        # Load products from JSON file
        json_path = os.path.join('data', 'products.json')
        try:
            with open(json_path, 'r') as f:
                data = json.load(f)
                
            if 'products' not in data:
                print("Error: Invalid JSON format - 'products' key not found")
                return
                
            products_data = data['products']
            print(f"Found {len(products_data)} products in JSON file")
            
            # Import products and product codes
            for product_data in products_data:
                # Create product
                product = Product(
                    id=product_data.get('id'),
                    category=product_data.get('category', ''),
                    collection=product_data.get('collection', ''),
                    item_name=product_data.get('item_name', ''),
                    dimensions=product_data.get('dimensions', ''),
                    price=product_data.get('price', ''),
                    notes=product_data.get('notes', '')
                )
                db.session.add(product)
                
                # Create product codes
                for code_data in product_data.get('product_codes', []):
                    code = ProductCode(
                        code=code_data.get('code', ''),
                        color=code_data.get('color', ''),
                        product_id=product.id
                    )
                    db.session.add(code)
            
            # Commit all changes to database
            db.session.commit()
            print(f"Successfully imported {len(products_data)} products to database!")
            
        except FileNotFoundError:
            print(f"Error: {json_path} not found.")
        except json.JSONDecodeError:
            print(f"Error: {json_path} is not valid JSON.")
        except Exception as e:
            print(f"Error during import: {str(e)}")
            db.session.rollback()

if __name__ == '__main__':
    import_products_from_json()
