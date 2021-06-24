import os

from flask import send_from_directory, render_template

from config import app, db
from api_v1 import api_v1


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/css/<filename>')
def get_css(filename):
    return send_from_directory(app.static_folder + '/css/', filename)


@app.route('/js/<filename>')
def get_js(filename):
    return send_from_directory(app.static_folder + '/js/', filename)


app.register_blueprint(api_v1)

if __name__ == '__main__':
    db.create_all()
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
