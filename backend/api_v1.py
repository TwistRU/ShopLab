import datetime
from io import BytesIO
from flask import request

from PIL import Image

from flask import Blueprint
from flask_cors import CORS
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask_restful import Resource, reqparse, Api
from sqlalchemy.exc import IntegrityError

from backend.config import db
from backend.database import ItemDB, Transactions, ImageDB
from backend.methods import user_is_admin_required, next_path

api_v1 = Blueprint('API_v1', __name__, url_prefix='/api/v1')
api = Api(api_v1)

CORS(api_v1, methods=['GET_LIST', 'HEAD', 'POST', 'OPTIONS', 'PUT', 'PATCH', 'DELETE', "GET_INFO"])


@api.resource('/item', methods=["GET_INFO", "GET_LIST", "POST", "PATCH", "DELETE"])
class ItemF(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('item_id')
    parser.add_argument('image')
    parser.add_argument('name')
    parser.add_argument('more_info')
    parser.add_argument('price')
    parser.add_argument('available')
    parser.add_argument('rating')
    parser.add_argument('page')
    parser.add_argument('page_limit')

    def get_info(self):
        item_id = self.parser.parse_args()['item_id']
        item = ItemDB.query.filter_by(item_id=item_id).first()
        if item is None:
            return {'error': 'Bad Request'}, 400
        return {'product': item.to_dict()}, 200

    def get_list(self):
        args = self.parser.parse_args()
        page = int(args['page'])
        page_limit = int(args['page_limit'])
        item = (
            ItemDB.query
                .offset((page - 1) * page_limit)
                .limit(page_limit)
        )
        if item is None:
            return {'error': 'Bad Request'}, 400
        return {
                   'products': [el.to_dict() for el in item],
                   'countOfAllItems': ItemDB.query.count()
               }, 200

    @user_is_admin_required
    def post(self):
        args = {key: val for key, val in self.parser.parse_args().items()
                if key in ('image', 'name', 'more_info', 'price', 'available', 'rating')}
        args['image_id'] = str(hash(args['image']))
        image = ImageDB(image_id=args['image_id'], imageB64=args['image'])

        args.pop('image')

        item = ItemDB(**args)
        db.session.add(item)
        db.session.add(image)
        try:
            db.session.commit()
        except IntegrityError:
            return {'status': 'Bad Request'}, 400

        return {'status': 'ok'}, 200

    @user_is_admin_required
    def patch(self):
        args = {key: val for key, val in self.parser.parse_args().items()
                if key in ('item_id', 'image', 'name', 'more_info', 'price', 'available', 'rating')}

        item_id = args['item_id']
        args.pop('item_id')
        item = ItemDB.query.filter_by(item_id=item_id).update(
            {key: val for key, val in args.items() if val is not None})
        db.session.commit()
        return {'status': 'ok'}, 200

    @user_is_admin_required
    def delete(self):
        item_id = self.parser.parse_args()['item_id']
        item = ItemDB.query.filter_by(item_id=item_id).first()
        image = ImageDB.query.filter_by(image_id=item.image_id)
        db.session.delete(image)
        db.session.delete(item)
        db.session.commit()
        return {'status': 'ok'}


@api.resource('/buy', methods=['POST'])
class BuyF(Resource):
    @jwt_required()
    def post(self):
        json = request.get_json()
        try:
            cart = json['items']
        except TypeError:
            return {'error': 'Bad Request'}, 400
        cost = 0
        for item_cart in cart:
            item = ItemDB.query.filter_by(item_id=item_cart['item_id']).first()
            if item is None:
                return {"error": "no item"}, 400
            if item.available >= int(item_cart['quantity']):
                cost += item_cart['quantity'] * item.price
                ItemDB.query.filter_by(item_id=item_cart['item_id']).update({
                    'available': item.available - item_cart['quantity']})

        transaction = Transactions(
            user_id=get_jwt_identity(),
            items=json,
            cost=cost,
            date=int((datetime.datetime.utcnow() - datetime.datetime(1970, 1, 1)).total_seconds())
        )
        db.session.add(transaction)
        db.session.commit()
        return {'transaction_id': transaction.transaction_id}
