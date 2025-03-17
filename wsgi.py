from app import create_app
from models import db

app = create_app()

# Initialize the database within the application context
with app.app_context():
    db.create_all()
    print("Database tables created successfully!")

if __name__ == "__main__":
    app.run()
