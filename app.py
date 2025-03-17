import os
import json
from flask import Flask, render_template, request, redirect, url_for, jsonify, session, flash
from flask_migrate import Migrate
from models import db, Product, ProductCode, Presentation

def create_app(test_config=None):
    # Create and configure the app
    app = Flask(__name__)
    
    # Configuration
    app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'dev_key_for_testing')
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///kbd_services.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Initialize database
    db.init_app(app)
    migrate = Migrate(app, db)
    
    # Create database tables (if they don't exist)
    with app.app_context():
        db.create_all()
    
    # Register routes
    register_routes(app)
    
    return app

# Load product data from JSON (fallback if database is not used)
def load_products():
    try:
        with open(os.path.join('data', 'products.json'), 'r') as f:
            return json.load(f)
    except Exception as e:
        print(f"Error loading products: {e}")
        return {"products": []}

def register_routes(app):
    # Route for home page
    @app.route('/')
    def index():
        return render_template('index.html')

    # Route for client requirements form
    @app.route('/client_form', methods=['GET', 'POST'])
    def client_form():
        if request.method == 'POST':
            # Process form data
            client_data = {
                'name': request.form.get('client_name'),
                'company': request.form.get('company_name'),
                'product_categories': request.form.getlist('product_categories'),
                'budget': request.form.get('budget'),
                'purpose': request.form.get('purpose'),
                'timeline': request.form.get('timeline')
            }
            
            # Store in session for use across routes
            session['client_data'] = client_data
            
            # Redirect to product selection
            return redirect(url_for('product_selection'))
        
        # If GET request, load the form
        # Extract unique categories for form options
        categories = set()
        
        # Try to get categories from database
        try:
            products = Product.query.all()
            if products:
                for product in products:
                    categories.add(product.category)
            else:
                # Fallback to JSON if database is empty
                products_data = load_products()
                for product in products_data['products']:
                    categories.add(product['category'])
        except:
            # Fallback to JSON if database query fails
            products_data = load_products()
            for product in products_data['products']:
                categories.add(product['category'])
        
        return render_template('client_form.html', categories=sorted(categories))

    # Route for product selection based on client requirements
    @app.route('/product_selection', methods=['GET'])
    def product_selection():
        # Get client data from session
        client_data = session.get('client_data', {})
        if not client_data:
            return redirect(url_for('client_form'))
        
        # Filter products based on client preferences
        filtered_products = []
        selected_categories = client_data.get('product_categories', [])
        
        # Try to get products from database
        try:
            if selected_categories:
                # If categories are selected, filter by them
                for category in selected_categories:
                    category_products = Product.query.filter_by(category=category).all()
                    filtered_products.extend(category_products)
            else:
                # If no categories selected, show all products
                filtered_products = Product.query.all()
                
            # Group products by category for easier display
            products_by_category = {}
            for product in filtered_products:
                category = product.category
                if category not in products_by_category:
                    products_by_category[category] = []
                products_by_category[category].append(product)
                
        except Exception as e:
            # Fallback to JSON if database query fails
            print(f"Database query error: {e}")
            products_data = load_products()
            
            # Filter products based on client preferences
            if selected_categories:
                for product in products_data['products']:
                    if product['category'] in selected_categories:
                        filtered_products.append(product)
            else:
                # If no categories selected, show all products
                filtered_products = products_data['products']
            
            # Group products by category for easier display
            products_by_category = {}
            for product in filtered_products:
                category = product['category']
                if category not in products_by_category:
                    products_by_category[category] = []
                products_by_category[category].append(product)
        
        # Add a flash message if no products were found
        if not filtered_products:
            flash("No products found matching the selected categories. Showing all available products instead.", "warning")
            # Show all products instead (try database first, then JSON)
            try:
                all_products = Product.query.all()
                if all_products:
                    products_by_category = {}
                    for product in all_products:
                        category = product.category
                        if category not in products_by_category:
                            products_by_category[category] = []
                        products_by_category[category].append(product)
                else:
                    # Fallback to JSON
                    products_data = load_products()
                    for product in products_data['products']:
                        category = product['category']
                        if category not in products_by_category:
                            products_by_category[category] = []
                        products_by_category[category].append(product)
            except:
                # Fallback to JSON
                products_data = load_products()
                for product in products_data['products']:
                    category = product['category']
                    if category not in products_by_category:
                        products_by_category[category] = []
                    products_by_category[category].append(product)
        
        return render_template('product_selection.html', 
                            products_by_category=products_by_category, 
                            client_data=client_data)

    # Route for creating presentations - accepts both GET and POST
    @app.route('/create_presentation', methods=['GET', 'POST'])
    def create_presentation():
        """Create a presentation from selected products."""
        print(f"Method: {request.method}")
        print(f"Form data: {request.form}")
        
        # For GET requests, redirect to product selection
        if request.method == 'GET':
            return redirect(url_for('product_selection'))
        
        # Handle POST request
        try:
            # Get client data from session
            client_data = session.get('client_data', {})
            
            # Get selected products
            selected_product_ids = request.form.getlist('selected_products')
            print(f"Selected products IDs: {selected_product_ids}")
            
            # Convert to integers
            product_ids = []
            for id_str in selected_product_ids:
                try:
                    product_ids.append(int(id_str))
                except ValueError:
                    print(f"Invalid product ID: {id_str}")
            
            # Create a new presentation in the database
            presentation = Presentation(
                client_name=client_data.get('name', ''),
                company_name=client_data.get('company', ''),
                budget=client_data.get('budget', ''),
                purpose=client_data.get('purpose', ''),
                timeline=client_data.get('timeline', ''),
                unique_link=Presentation.generate_unique_link()
            )
            
            # Add selected products to the presentation
            try:
                for product_id in product_ids:
                    product = Product.query.get(product_id)
                    if product:
                        presentation.products.append(product)
            except Exception as e:
                print(f"Error adding products to presentation: {e}")
                # Store selected products in session as fallback
                session['selected_product_ids'] = product_ids
            
            # Save presentation to database
            try:
                db.session.add(presentation)
                db.session.commit()
                print(f"Created presentation with link: {presentation.unique_link}")
                
                # Redirect to presentation view using unique link
                return redirect(url_for('presentation_by_link', link=presentation.unique_link))
            except Exception as e:
                print(f"Error saving presentation: {e}")
                db.session.rollback()
                
                # Fallback to using presentation_id
                session['selected_product_ids'] = product_ids
                return redirect(url_for('presentation', presentation_id=1))
        except Exception as e:
            print(f"Error creating presentation: {e}")
            # If there's an error, redirect back to selection
            return redirect(url_for('product_selection'))

    # Route for presentation view (by ID - legacy/fallback method)
    @app.route('/presentation/<int:presentation_id>')
    def presentation(presentation_id):
        # Get client data and selected products from session
        client_data = session.get('client_data', {})
        selected_product_ids = session.get('selected_product_ids', [])
        
        # Get products from database or JSON
        try:
            # Try to load products from database
            all_products = Product.query.all()
            if all_products:
                # Filter to just selected products
                selected_products = []
                for product in all_products:
                    if product.id in selected_product_ids:
                        selected_products.append(product)
                
                # If no products selected, show a default selection
                if not selected_products and all_products:
                    selected_products = all_products[:4]
            else:
                # Fallback to JSON
                raise Exception("No products in database")
        except Exception as e:
            print(f"Database query error: {e}")
            # Fallback to JSON
            products_data = load_products()
            all_products = products_data.get('products', [])
            
            # Filter to just selected products
            selected_products = []
            for product in all_products:
                if product['id'] in selected_product_ids:
                    selected_products.append(product)
            
            # If no products selected, show a default selection
            if not selected_products and all_products:
                selected_products = all_products[:4]
        
        return render_template('presentation.html', 
                            products=selected_products,
                            client_data=client_data,
                            presentation_id=presentation_id)
    
    # New route for presentation view by unique link
    @app.route('/p/<link>')
    def presentation_by_link(link):
        # Find presentation by unique link
        try:
            presentation = Presentation.query.filter_by(unique_link=link).first()
            if not presentation:
                flash("Presentation not found", "error")
                return redirect(url_for('index'))
            
            # Get client data from presentation
            client_data = {
                'name': presentation.client_name,
                'company': presentation.company_name,
                'budget': presentation.budget,
                'purpose': presentation.purpose,
                'timeline': presentation.timeline
            }
            
            # Get products from presentation
            selected_products = presentation.products
            
            return render_template('presentation.html', 
                                products=selected_products,
                                client_data=client_data,
                                presentation_id=presentation.id,
                                unique_link=link)
        except Exception as e:
            print(f"Error loading presentation by link: {e}")
            flash("Error loading presentation", "error")
            return redirect(url_for('index'))

# Create the application
app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
