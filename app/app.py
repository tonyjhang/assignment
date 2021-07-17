from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .apis import api_blueprint
from .config.db import config 

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = config
db = SQLAlchemy(app)
app.register_blueprint(api_blueprint, url_prefix='')