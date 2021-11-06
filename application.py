from flask import Flask

application = Flask(__name__)


@application.route('/')
def hello_world():
    return 'AWWWWWW YEEEEAAAAAHHHHHHH. Will this work?'
