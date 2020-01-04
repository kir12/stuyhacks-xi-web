from config import Config
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

#get app instance
app = Flask(__name__)

#import database assets and set accessible instances of both
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)


#"pass" request to Controller and Model
from voteapp import routes,models
