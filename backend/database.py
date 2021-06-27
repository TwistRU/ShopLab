from sqlalchemy import orm
from sqlalchemy.dialects.postgresql import JSON

from backend.config import db


class Transactions(db.Model):
    __tablename__ = 'transactions'
    query: orm.Query

    transaction_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False)
    items = db.Column(JSON, nullable=False)
    cost = db.Column(db.Integer, nullable=False)
    date = db.Column(db.Integer, nullable=False)


class UserDB(db.Model):
    __tablename__ = 'users'
    query: orm.Query

    user_id = db.Column(db.Integer, unique=True, primary_key=True, autoincrement=True)
    first_name = db.Column(db.String, nullable=False)
    second_name = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False)
    login = db.Column(db.String, nullable=False, primary_key=True, unique=True)
    password_hash = db.Column(db.String, nullable=False)
    role = db.Column(db.Integer, nullable=False, default=0)  # 0 = user, 1 = admin, 2 = ban


class ItemDB(db.Model):
    __tablename__ = 'items'
    query: orm.Query

    item_id: int = db.Column(db.Integer, primary_key=True, autoincrement=True)
    image_id: int = db.Column(db.String, db.ForeignKey('images.image_id'))
    name: str = db.Column(db.String, nullable=False)
    more_info: str = db.Column(db.String)
    price: float = db.Column(db.Float, nullable=False)
    available: int = db.Column(db.Integer, nullable=False)
    rating: float = db.Column(db.Float, nullable=False)

    def to_dict(self):
        return {
            'item_id': self.item_id,
            'image_id': self.image_id,
            'name': self.name,
            'more_info': self.more_info,
            'price': self.price,
            'available': self.available,
            'rating': self.rating
        }


class ImageDB(db.Model):
    __tablename__ = 'images'
    query = orm.Query

    image_id = db.Column(db.String, primary_key=True)
    imageB64 = db.Column(db.String, nullable=False)
