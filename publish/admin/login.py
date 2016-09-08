from flask import render_template, request, redirect, url_for


from . import admin

from lib.user import User

import flask_login


@admin.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        userName = request.form['userName']
        password = request.form['password']
        user = User.validUser(userName, password)
        if user == None:
            return redirect(url_for('.login'))
        flask_login.login_user(user)
        return redirect(url_for('.index'))
    else:
        return render_template('login.html')


@admin.route('/logout')
@flask_login.login_required
def logout():
    logout_user()
    return redirect(url_for('public_timeline'))
