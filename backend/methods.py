from functools import wraps

from flask_jwt_extended import jwt_required, get_jwt_identity

from backend.database import UserDB


def user_is_admin_required(func):
    @wraps(func)
    @jwt_required()
    def check_user_is_admin(*args, **kwargs):
        user_id = get_jwt_identity()
        print(user_id)
        user = UserDB.query.filter_by(user_id=user_id).first()
        if user.role == 1:
            return func(*args, **kwargs)
        else:
            return {'error': 'Forbidden'}, 403

    return check_user_is_admin
