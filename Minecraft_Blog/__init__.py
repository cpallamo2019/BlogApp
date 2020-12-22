#Minecraft_Blog/__init__.py

from flask import Flask

app=Flask(__name__)


from Minecraft_Blog.core.views import core

app.register_blueprint(core)
