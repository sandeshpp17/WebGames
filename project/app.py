from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient
import os

app = Flask(__name__)

# Connect to MongoDB
MONGO_URI = os.environ.get('MONGO_URI', 'mongodb://172.16.22.103:27017/')
client = MongoClient(MONGO_URI)
db = client['webgames']  # Create or use a database named 'webgames'
users_collection = db['users']  # Create or use a collection named 'users'

@app.route('/')
def login():
    """Render the login page."""
    return render_template('login.html')

@app.route('/home/')
def home():
    """Render the home page."""
    return render_template('home.html')

@app.route('/register/', methods=['GET', 'POST'])
def register():
    """Render the registration page and handle user registration."""
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        
        # Check if the username or email already exists in the database
        existing_user = users_collection.find_one({'$or': [{'username': username}, {'email': email}]})
        if existing_user:
            return "Username or email already exists!"
        
        # Insert the new user into the database
        new_user = {'username': username, 'email': email, 'password': password}
        users_collection.insert_one(new_user)
        
        return redirect(url_for('login'))  # Redirect to the login page after successful registration
    else:
        return render_template('register.html')

@app.route('/logout/')
def logout():
    """Handle user logout."""
    # Implement logout logic here
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)
