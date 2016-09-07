from flask import render_template

from . import admin

import flask_login

from lib.db import DB

db = DB()


@admin.route('/user')
@flask_login.login_required
def user():
    sql = 'SELECT * FROM ly_users'
    users = db.query(sql).getAll()
    return render_template('user.html', users=users)


@admin.route('/user/add')
@flask_login.login_required
def add():
    return render_template('edit.html', user={})


@admin.route('/user/edit/<id>')
@flask_login.login_required
def edit(id):
    sql = 'SELECT * FROM ly_users WHERE id={0}'.format(id)
    _user = db.query(sql).getRow()
    return render_template('user_edit.html', user=_user)
