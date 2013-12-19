from flask import Flask
from flask.ext.mongoengine import MongoEngine
import os,urlparse


MONGOLAB_URI = os.environ.get('MONGOLAB_URI')
url = urlparse.urlparse(MONGOLAB_URI)
MONGODB_USER = url.username
MONGODB_PASSWORD = url.password
MONGODB_HOST = url.hostname
MONGODB_PORT = url.port
MONGODB_DB = url.path[1:]




app = Flask(__name__)
app.config["MONGODB_SETTINGS"] = {"DB": MONGODB_DB,
    "USERNAME": MONGODB_USER,
    "PASSWORD": MONGODB_PASSWORD,
    "HOST"    : MONGODB_HOST,
    "PORT"    : MONGODB_PORT
    }
app.config["SECRET_KEY"] = "KeepThisS3cr3t"

db = MongoEngine(app)


def register_blueprints(app):
    # Prevents circular imports
    from tumblelog.views import posts
    from tumblelog.admin import admin
    app.register_blueprint(posts)
    app.register_blueprint(admin)

register_blueprints(app)

if __name__ == '__main__':
    app.run()
