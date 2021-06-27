from io import BytesIO
from PIL import Image

from flask import Blueprint
from flask_cors import CORS
from flask_restful import Resource, reqparse, Api
from sqlalchemy.exc import IntegrityError

from backend.config import db
from backend.database import ItemDB, UserDB
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
        print(item)
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
        return {'products': [el.to_dict() for el in item]}, 200

    @user_is_admin_required
    def post(self):
        args = {key: val for key, val in self.parser.parse_args().items()
                if key in ('image', 'name', 'more_info', 'price', 'available', 'rating')}
        bytes_io_image = BytesIO(bytes(args['image'], encoding='raw_unicode_escape'))
        image = Image.open(bytes_io_image)
        image_path = '../dist/image/'
        image_name = next_path(image_path, str(hash(bytes_io_image)) + '(%s).' + image.format)
        image.save(image_path + image_name)
        args['image'] = image_name

        item = ItemDB(**args)
        db.session.add(item)
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
        db.session.delete(item)
        db.session.commit()
        return {'status': 'ok'}
