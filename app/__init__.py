from flask import Flask
from .config import DevConfig

#initialize the application
app=Flask(__name__)

# Setting up the configuration

from app import views