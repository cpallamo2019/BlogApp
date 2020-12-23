#Minecraft_Blog/__init__.py

from flask import Flask

app=Flask(__name__)


from Minecraft_Blog.core.views import core
from Minecraft_Blog.error_pages.handlers import error_pages

app.register_blueprint(error_pages)
app.register_blueprint(core)
