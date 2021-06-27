import os

from flask import send_from_directory, render_template

from backend.config import app, db
from backend.api_v1 import api_v1
from backend.authorization import authBP
from backend.database import ImageDB


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/css/<filename>')
def get_css(filename):
    return send_from_directory(app.static_folder + '/css/', filename)


@app.route('/js/<filename>')
def get_js(filename):
    return send_from_directory(app.static_folder + '/js/', filename)


@app.route('/image/<image_id>')
def get_image(image_id):
    image = db.session.execute('SELECT * FROM images WHERE image_id = :val', {'val': image_id})
    for r in image:
        image = r['imageB64']
        break
    return image


app.register_blueprint(api_v1)
app.register_blueprint(authBP)

if __name__ == '__main__':
    db.create_all()
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
