# __init__ file makes the folder into an executable python package that we are able to import and run

from flask import Flask

def create_app():
    app = Flask(__name__)
    # Encrypt the cookie and session data
    app.config['SECRET_KEY'] = 'asdsadkdfjg1@#!sdfsdf'

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix = '/')
    app.register_blueprint(auth, url_prefix = '/') #no prefix is set

    return app