from flask import Flask


app = Flask(__name__)

from controllers import default
from controllers import predict

