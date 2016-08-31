from flask import Flask
from assets import assets
from admin import admin

app = Flask(__name__)

app.register_blueprint(assets)

app.register_blueprint(admin, url_prefix='/admin')

if __name__ == '__main__':
    app.run()
