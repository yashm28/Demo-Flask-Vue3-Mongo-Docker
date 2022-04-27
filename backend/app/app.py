from flask import Flask
from flask_cors import CORS, cross_origin
from models.db import db
from controllers import api
# from werkzeug.middleware.proxy_fix import ProxyFix

app = Flask(__name__)
# cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
app.config['MONGODB_SETTINGS'] = {
    'db': 'posts',
    'host': 'mongo-db',
    'port': 27017,
    'username': 'root',
    'password': 'example',
}
db.init_app(app)
api.init_app(app)
# app.wsgi_app = ProxyFix(app.wsgi_app, x_proto=1, x_port=1, x_for=1, x_host=1, x_prefix=1)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)