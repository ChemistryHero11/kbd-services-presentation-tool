# KBD Services Promotional Products Presentation Tool

A Flask-based web application for creating and sharing customized product presentations for clients.

## Features

- **Client-Specific Presentations**: Create tailored presentations based on client requirements
- **Product Filtering**: Filter products by category to match client needs
- **Shareable Links**: Generate unique links to share presentations with clients
- **Professional Branding**: Consistent KBD Services branding throughout the application
- **Responsive Design**: Works on multiple devices for presenting anywhere

## Technologies

- Python/Flask
- SQLite Database
- SQLAlchemy ORM
- HTML/CSS/Bootstrap
- JavaScript

## Getting Started

1. Clone the repository
2. Install dependencies: `pip install -r requirements.txt`
3. Initialize the database: 
   ```
   flask --app app.py db init
   flask --app app.py db migrate
   flask --app app.py db upgrade
   ```
4. Import product data: `python import_data_script.py`
5. Start the development server: `python app.py`

## Project Structure

- `/templates`: HTML templates for the application
  - `index.html`: Homepage
  - `client_form.html`: Client requirements form
  - `product_selection.html`: Product selection interface
  - `presentation.html`: Final presentation view
- `/static`: Static assets (CSS, JavaScript, images)
- `/data`: JSON data files
- `/models.py`: Database models
- `/app.py`: Main application code

## Deployment

This application can be deployed using:
- Render
- PythonAnywhere
- Heroku
- Any other Flask-compatible hosting service
