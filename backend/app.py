import traceback  # Import traceback module
import os
from flask import Flask, request, jsonify, render_template
from flask_pymongo import PyMongo

# app = Flask(__name__, template_folder='/frontend/templates', static_folder='/frontend/static')
app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://db:27017/mydatabase"  # Use the service name 'db' to connect to MongoDB in Docker Compose
mongo = PyMongo(app)

# Specify the templates directory explicitly
template_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'frontend', 'templates'))
# template_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), 'frontend', 'templates'))
# app.template_folder = template_dir
app.template_folder = template_dir

# Specify the static directory explicitly
static_dir = os.path.abspath(os.path.join(os.path.dirname(__file__),'..', 'frontend', 'static'))
app.static_folder = static_dir


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    try:
        data = request.json
        name = data.get('name')
        email = data.get('email')

        if name and email:
            mongo.db.users.insert_one({"name": name, "email": email})
            return jsonify({"message": "Data stored successfully"}), 200
        else:
            return jsonify({"error": "Name and email are required fields"}), 400
    except Exception as e:
        traceback.print_exc()  # Print traceback to console for debugging
        return jsonify({"error": "Internal server error"}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')  # Listen on all interfaces for Docker compatibility






# from flask import Flask, render_template
# from flask_pymongo import PyMongo
# import os

# app = Flask(__name__)

# # Set the template folder explicitly
# template_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'frontend', 'templates'))
# app.template_folder = template_dir

# # Initialize PyMongo
# app.config["MONGO_URI"] = "mongodb://db:27017/mydatabase"
# mongo = PyMongo(app)

# # Define routes
# @app.route('/')
# def index():
#     return render_template('index.html')

# @app.route('/submit', methods=['POST'])
# def submit():
#     # Handle form submission
#     pass

# if __name__ == '__main__':
#     app.run(debug=True, host='0.0.0.0')
