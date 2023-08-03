from flask import Flask, render_template, request, redirect, url_for
import pymongo
import mongoClient 

app = Flask(__name__)
client = MongoClient('mongodb://localhost:27017/')  # Update with your MongoDB connection string
db = client['login_db']
users_collection = db['users']

@app.route('/')
def login_page():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    # Check if the user exists in the database
    user = users_collection.find_one({'username': username, 'password': password})

    if user:
        # Handle successful login (redirect to a dashboard page, for example)
        return "Login successful!"
    else:
        # Handle failed login (display an error message or redirect to the login page)
        return "Invalid username or password."

if __name__ == '__main__':
    app.run(debug=True)
