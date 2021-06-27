import os

from datetime import timedelta

from flask import Flask
from flask_bcrypt import Bcrypt

from flask_sqlalchemy import SQLAlchemy

from flask_jwt_extended import JWTManager

from flask_cors import CORS

app = Flask(__name__, template_folder='../dist/', static_folder='../dist/')

salt = os.environ.get('SALT')
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')

app.config['JWT_SECRET_KEY'] = os.environ.get('JWT_SECRET_KEY')
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(hours=1)
app.config['JWT_REFRESH_TOKEN_EXPIRES'] = timedelta(days=30)

DATABASE_URL = os.environ['DATABASE_URL'].replace('postgres', 'postgresql', 1)

app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URL
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

jwt = JWTManager(app)
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
CORS(app)

try:
    os.mkdir('../dist/image')
except Exception as e:
    print(e)
