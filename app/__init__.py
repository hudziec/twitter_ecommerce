#set up imports
from flask import Flask
from flask_bootstrap import Bootstrap
from config import Config


#setup app variables
app = Flask(__name__)
bootstrap = Bootstrap(app)
app.config.from_object(Config)


#go to routes
from app import routes
#
