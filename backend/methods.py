import os

from functools import wraps

from flask_jwt_extended import jwt_required, get_jwt_identity

from backend.database import UserDB


def user_is_admin_required(func):
    @wraps(func)
    @jwt_required()
    def check_user_is_admin(*args, **kwargs):
        user_id = get_jwt_identity()
        user = UserDB.query.filter_by(user_id=user_id).first()
        if user.role == 1:
            return func(*args, **kwargs)
        else:
            return {'error': 'Forbidden'}, 403

    return check_user_is_admin


def next_path(path, file_name_pattern):
    """
    Finds the next free path in an sequentially named list of files

    e.g. file_name_pattern = 'file-%s.txt':

    file-1.txt
    file-2.txt
    file-3.txt

    Runs in log(n) time where n is the number of existing files in sequence
    """
    i = 1

    # First do an exponential search
    while os.path.exists(path + file_name_pattern % i):
        i = i * 2

    # Result lies somewhere in the interval (i/2..i]
    # We call this interval (a..b] and narrow it down until a + 1 = b
    a, b = (i // 2, i)
    while a + 1 < b:
        c = (a + b) // 2  # interval midpoint
        a, b = (c, b) if os.path.exists(path + file_name_pattern % c) else (a, c)

    return file_name_pattern % b
