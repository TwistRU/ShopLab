from flask import request, Blueprint
from flask_jwt_extended import create_access_token, create_refresh_token
from flask_restful import Resource, reqparse
from sqlalchemy.exc import IntegrityError

from backend.config import bcrypt, db
from backend.database import UserDB

authBP = Blueprint('authBP', __name__, url_prefix='/auth')


@authBP.route('registration', methods=['POST'])
def registration():
    parser = reqparse.RequestParser()
    parser.add_argument('first_name', required=True)
    parser.add_argument('second_name', required=True)
    parser.add_argument('email', required=True)
    parser.add_argument('login', required=True)
    parser.add_argument('password', required=True)

    args = parser.parse_args()
    password_hash = bcrypt.generate_password_hash(args['password']).decode('utf8')
    args.pop('password')
    new_user = UserDB(password_hash=password_hash, **args)
    db.session.add(new_user)
    try:
        db.session.commit()
    except IntegrityError:
        return {'error': 'login is already taken'}, 400
    return {'status': 'ok'}, 200


@authBP.route('login', methods=["POST"])
def login():
    parser = reqparse.RequestParser()
    parser.add_argument('login', required=True)
    parser.add_argument('password', required=True)

    args = parser.parse_args()
    user = UserDB.query.filter_by(login=args['login']).first()
    if user is None or not bcrypt.check_password_hash(user.password_hash, args['password']):
        return {'error': 'Email or password invalid'}, 401
    access_token = create_access_token(user.user_id)
    refresh_token = create_refresh_token(user.user_id)
    return {
        'access_token': access_token,
        'refresh_token': refresh_token
    }, 200
