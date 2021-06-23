import os

from datetime import timedelta

from flask import Flask
from flask_restful import Api

from flask_jwt_extended import create_access_token, create_refresh_token, get_jwt_identity, jwt_required, JWTManager

app = Flask(__name__)

api = Api(app)

salt = os.environ.get('SALT')
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')

app.config['JWT_SECRET_KEY'] = os.environ.get('JWT_SECRET_KEY')
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(hours=1)
app.config['JWT_REFRESH_TOKEN_EXPIRES'] = timedelta(days=30)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
jwt = JWTManager(app)

if __name__ == '__main__':
    app.run(debug=True)
