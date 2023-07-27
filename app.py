import requests
import json
from flask import Flask
from sqlalchemy import SQLAlchemy

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
db = SQLAlchemy(app)

 # Create a Flask application instance
app = Flask(__name__)
 # Lets connect to a database
class Books(db.model):
    id = db.column(db.integer, primary_key=True)
    name = db.column(db.string(80), unique=True, nullable=True)
    
    def __repr__(self):
        return f"{self.name} - {self.description}" 
 
 
app.route('/') 
def index():
    return "Hello"

app.route('/books')
def get_books():
    
    return {"books": "books_data" }





