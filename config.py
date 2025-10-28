import os
import connexion
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_jwt_extended import JWTManager
from flask_cors import CORS

basedir = os.path.abspath(os.path.dirname(__file__))

# Create the connexion application instance
connex_app = connexion.App(__name__, specification_dir='./templates')

# Get the underlying Flask app instance
app = connex_app.app
CORS(app)

# Configure the SqlAlchemy part of the app instance
app.config["SQLALCHEMY_ECHO"] = True
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///orders.db')
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config['JWT_SECRET_KEY'] = 'mdhs.me'

# JWT instance
jwt = JWTManager(app)

# Create the SqlAlchemy db instance
db = SQLAlchemy(app)

# Initialize Marshmallow
ma = Marshmallow(app)
