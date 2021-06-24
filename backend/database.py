from sqlalchemy import orm

from config import db


class UserDB(db.Model):
    __tablename__ = 'users'
    query: orm.Query

    user_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_name = db.Column(db.String, nullable=False)
    second_name = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False)
    login = db.Column(db.String, nullable=False)
    password_hash = db.Column(db.String, nullable=False)
    role = db.Column(db.Integer, nullable=False)


class ItemDB(db.Model):
    __tablename__ = 'items'
    query: orm.Query

    item_id: int = db.Column(db.Integer, primary_key=True, autoincrement=True)
    image: str = db.Column(db.String, nullable=False)
    name: str = db.Column(db.String, nullable=False)
    more_info: str = db.Column(db.String)
    price: float = db.Column(db.Float, nullable=False)
    available: int = db.Column(db.Integer, nullable=False)
    rating: float = db.Column(db.Float, nullable=False)

    def to_dict(self):
        return {
            'item_id': self.item_id,
            'image': self.image,
            'name': self.name,
            'more_info': self.more_info,
            'price': self.price,
            'available': self.available,
            'rating': self.rating
        }
