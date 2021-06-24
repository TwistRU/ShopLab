import os

from datetime import timedelta

from flask import Flask

from flask_sqlalchemy import SQLAlchemy

from flask_jwt_extended import JWTManager

from flask_cors import CORS

app = Flask(__name__, template_folder='../dist/', static_folder='../dist/')

salt = os.environ.get('SALT')
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')

app.config['JWT_SECRET_KEY'] = os.environ.get('JWT_SECRET_KEY')
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(hours=1)
app.config['JWT_REFRESH_TOKEN_EXPIRES'] = timedelta(days=30)

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

jwt = JWTManager(app)
db = SQLAlchemy(app)
CORS(app)
