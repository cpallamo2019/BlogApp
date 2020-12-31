#Minecraft_Blog/__init__.py

import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager


app=Flask(__name__)
app.config['SECRET_KEY']='mysecret'

#####################
#DATABASE SETUP
####################

basedir= os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///'+os.path.join(basedir,'data.sqlite')
app.config['SQLACHEMY_TRACK_MODIFICATIONS']=False

db=SQLAlchemy(app)
Migrate(app,db)
######################
# LOGIN CONFIGS

login_manager=LoginManager()

login_manager.init_app(app)
login_manager.login_view='users.login'



from Minecraft_Blog.core.views import core
from Minecraft_Blog.error_pages.handlers import error_pages
from Minecraft_Blog.users.views import users

app.register_blueprint(users)
app.register_blueprint(error_pages)
app.register_blueprint(core)
