from flask import Flask
from assets import assets
from admin import admin

from lib.user import User

import flask_login


app = Flask(__name__)

login_manager = flask_login.LoginManager()

login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    return User.getUser(user_id)


@login_manager.unauthorized_handler
def unauthorized_user(user_id):
    return User.getUser(user_id)
# @login_manager.user_loader
# def user_loader(userName):
#     return User.getUser(userName)


# @login_manager.request_loader
# def request_loader(request):
#     email = request.form.get('email')
#     if email not in users:
#         return

#     user = User()
#     user.id = email

#     # DO NOT ever store passwords in plaintext and always compare password
#     # hashes using constant-time comparison!
#     user.is_authenticated = request.form['pw'] == users[email]['pw']

#     return user


# app.register_blueprint(assets)

app.register_blueprint(admin, url_prefix='/admin')
