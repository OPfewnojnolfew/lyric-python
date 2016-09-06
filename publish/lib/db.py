
# import pymysql.cursors

# from .config import config

# # Connect to the database


# def _getConnection():
#     return pymysql.connect(host=config.get('db', 'host'),
#                            port=config.getint('db', 'port'),
#                            user=config.get('db', 'user'),
#                            password=config.get('db', 'password'),
#                            db=config.get('db', 'database'),
#                            charset=config.get('db', 'charset'),
#                            cursorclass=pymysql.cursors.DictCursor)


# def query(sql):
#     connection = _getConnection()
#     try:
#         with connection.cursor() as cursor:
#             cursor.execute(sql)
#             return cursor.fetchone()
#     finally:
#         connection.close()


import pymysql
import re
from .config import config


class DB:
    corsr = None
    conn = None

    def __init__(self):

        # connect to mysql
        self.conn = pymysql.connect(host=config.get('db', 'host'),
                                    port=config.getint('db', 'port'),
                                    user=config.get('db', 'user'),
                                    password=config.get('db', 'password'),
                                    db=config.get('db', 'database'),
                                    charset=config.get('db', 'charset'),
                                    cursorclass=pymysql.cursors.DictCursor)

    def query(self, qstr, params=None):
        self.corsr = self.conn.cursor()
        with self.corsr as cursor:
            # do query results here
            if params == None:
                cursor.execute(qstr)
            else:
                cursor.execute(qstr, params)

            # check if query is not select
            if re.search("^([select|Select|SELECT])\w+", qstr) == None:
                self.conn.commit()
            return self

    def getRow(self):
        # get row function
        rs = self.corsr.fetchone()
        self.corsr.close()
        return rs

    def getAll(self):
        with self.corsr as cursor:
            result = cursor.fetchall()
            cursor.close()
            return result
    '''
        Force to close db connection
    '''

    def close(self):
        self.corsr.close()
        self.conn.close()
