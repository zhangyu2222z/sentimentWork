import datetime

# crt_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
# print(crt_time)


# cstr = '16小时前'

# tstr = '分钟'
# tstr2 = '小时'

# if tstr in cstr or tstr2 in cstr:
#     print('11111111111111111')

import pymysql
from snownlp import SnowNLP

# def test():
#     conn = pymysql.connect(host = '120.79.80.47', port = 3306, 
#                 user = 'root', password = 'root1234', db = 'zy')
#     try:
#         cur = conn.cursor()
#         # TODO
#         sqlStr = 'SELECT * FROM auth_user ' 
#         cur.execute(sqlStr)
#         result = cur.fetchall()
#         print(result)
#         print(type(result))
#         return result
#     except Exception as e:
#         conn.rollback()
#         print(e)
#     finally:
#         conn.close()
#     return ''

if __name__ == '__main__':
    vals = ((1, 'zhangy123456', 0, 'zhangy', 0, 1, datetime.datetime(2020, 8, 21, 2, 29, 54, 652721)), 
    (2, 'pbkdf2_sha256$216000$o4CYHB4a8aBz$l04ZbNDhqmLg3stYvAv0lixkB/ibig3TwG6DznvMYPU=',  0, 'zhangy2',  0, 1, datetime.datetime(2020, 8, 21, 3, 30, 41, 898988)), 
    (3, 'pbkdf2_sha256$150000$fcKnK8vOll7F$ANByaQfnJAxCRxJFqL+sItaU54IXT+kyYMH2ymnrIY8=',  1, 'admin',  1, 1, datetime.datetime(2020, 8, 26, 2, 58, 37, 696854)), 
    (4, 'pbkdf2_sha256$120000$XN6Dnn98JJiN$ZNzu0S9U+e54IWMF8nvbu/foyxlXDpHH6zrDjAUzgzE=', 1, 'zhangyu',  1, 1, datetime.datetime(2020, 8, 26, 9, 15, 47, 362457)))

    # print(vals[0][1])

    s = SnowNLP('狗东过分了，刚来变价')

    print(s.sentiments)