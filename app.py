import requests
import json
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Create a Flask application instance
app = Flask(__name__)

# Configure the SQLAlchemy database URI
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
# Create the SQLAlchemy instance and associate it with the app
db = SQLAlchemy(app)

# Lets connect to a database & create model for books
class Books(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=True)
    
    def __repr__(self):
        return f"{self.name} - {self.description}" 
 
 
app.route('/') 
def index():
    return "Hello"

app.route('/books', methods=['GET'])
def get_books():
    # Here you can fetch books data from the database
    # For now, I'll just return some sample data as a dictionary
     output = []
     for book in books:
         books_data = [
        {"name": "Book 1", "description": "This is book 1."},
        {"name": "Book 2", "description": "This is book 2."},
    
         ]
         output.append(books_data)
         
         return {"drinks": output}    
         
@app.route('/books/<id>')
def get_book(id):
    book = Book.query.get_or_404(id)
    return {"name": book.name, "description": drink.description}  

@app.route('/books', method=['POST'])
def add_book():
    book = Book(name=requests.json['name'], description=requests.json['description'])
    db.session.add(book)
    db.session.commit()
    
    return {'id': book.id}  


if __name__ == "__main__":
    app.run(debug=True, port=8000)






