from flask import Blueprint

assets = Blueprint(
    'assets',
    __name__,
    template_folder='templates',
    static_folder='static'
)

from . import home
