# import pymysql.cursors

# # Connect to the database
# connection = pymysql.connect(host='192.168.60.197',
#                              port=3306,
#                              user='root',
#                              password='',
#                              db='pvd_test',
#                              charset='utf8mb4',
#                              cursorclass=pymysql.cursors.DictCursor)


# def query(sql):
#     try:
#         with connection.cursor() as cursor:
#             cursor.execute(sql)
#             return cursor
#     finally:
#         connection.close()


import pymysql.cursors

from .config import config

# Connect to the database
connection = pymysql.connect(host=config.get('db', 'host'),
                             port=config.getint('db', 'port'),
                             user=config.get('db', 'user'),
                             password=config.get('db', 'password'),
                             db=config.get('db', 'database'),
                             charset=config.get('db', 'charset'),
                             cursorclass=pymysql.cursors.DictCursor)


def query(sql):
    try:
        with connection.cursor() as cursor:
            cursor.execute(sql)
            return cursor
    finally:
        connection.close()
