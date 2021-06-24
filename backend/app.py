from flask import send_from_directory, send_file, url_for, render_template

from backend.config import app


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/css/<filename>')
def get_css(filename):
    return send_from_directory(app.static_folder + '/css/', filename)


@app.route('/js/<filename>')
def get_js(filename):
    return send_from_directory(app.static_folder + '/js/', filename)


if __name__ == '__main__':
    app.run(debug=True)

