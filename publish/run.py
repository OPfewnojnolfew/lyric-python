import app
import os

if __name__ == '__main__':
    app.app.secret_key = os.urandom(24)
    app.app.run()
