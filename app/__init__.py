from flask import Flask
from .config import DevConfig

# initializing the app
app=Flask(__name__)

# settin up configuration
app.config.from_object(DevConfig)

from app import views
