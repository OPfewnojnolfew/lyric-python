from flask import render_template

from . import admin

import flask_login


@admin.route('/index')
@flask_login.login_required
def index():
    return render_template('index.html')
