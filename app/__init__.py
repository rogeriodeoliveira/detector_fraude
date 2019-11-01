from flask import Flask
import os


app = Flask(__name__)

SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY

from app.controllers import default
from app.controllers import predict

