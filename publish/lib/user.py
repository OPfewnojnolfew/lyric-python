import flask_login

from lib.db import DB

db = DB()


class User(flask_login.UserMixin):

    @staticmethod
    def getUser(id):
        sql = "SELECT * FROM ly_users WHERE id='{id}'".format(id=id)
        result = db.query(sql).getRow()
        # result = cursor.fetchone()
        user = User()
        if result['id']:
            user.id = result['id']
            user.name = result['name']
            user.loginName = result['loginName']
            return user
        else:
            return None

    @staticmethod
    def validUser(userName, password):
        if not userName == '' or not password == '':
            sql = "SELECT * FROM ly_users WHERE loginName='{userName}' AND password='{password}'".format(
                userName=userName, password=password)
            result = db.query(sql).getRow()
            if result != None:
                user = User()
                user.id = result['id']
                user.name = result['name']
                user.loginName = result['loginName']
                return user
            return result
