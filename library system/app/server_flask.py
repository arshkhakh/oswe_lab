#we build web server on Flask to handle the requests from login.py

# we need to save the index_flask.html file under templates folder (ALWAYS). Flask, by default, looks for template files (HTML files) in a folder named templates. This is by by convention.
# javascript file under /static
from flask import Flask, request, jsonify, render_template
from login1 import authenticate

app = Flask(__name__)

# Serve the frontend (index.html)
@app.route('/')
def home():
    return render_template('index_flask.html')

# Handle login form submission
@app.route('/login1', methods=['POST'])
def login():
    # Get username and password from the form
    username = request.form.get('username')
    password = request.form.get('password')

    # Authenticate the user
    if authenticate(username, password):
        return jsonify({"status": "success", "message": "Login successful"})
    else:
        return jsonify({"status": "error", "message": "Invalid username or password"}), 401

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True, port=8000)