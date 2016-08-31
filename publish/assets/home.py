from flask import render_template

from lib.db import query

from . import assets


@assets.route('/')
def index():
    sql = 'SELECT * FROM pvd_module WHERE STATUS_={status}'.format(
        status=1)
    cursor = query(sql)
    result = cursor.fetchall()
    return render_template('index.html', menus=result)
