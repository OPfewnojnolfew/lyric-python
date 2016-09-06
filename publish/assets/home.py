from flask import render_template

from lib.db import DB

db = DB()


from . import assets


@assets.route('/')
def index():
    sql = 'SELECT * FROM pvd_module WHERE STATUS_={status}'.format(
        status=1)
    result = db.query(sql).getAll()
    return render_template('index.html', menus=result)
