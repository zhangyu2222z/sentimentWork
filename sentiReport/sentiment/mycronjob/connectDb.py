import pymysql
import configparser

class ConnDb():
    def __init__(self):
        config = configparser.ConfigParser()
        config.read('./mycronjob/properties.conf', encoding='utf-8')
        self.host = config.get('mysql', 'host')
        self.port = config.get('mysql', 'port')
        self.user = config.get('mysql', 'user')
        self.password = config.get('mysql', 'password')
        self.db = config.get('mysql', 'db')
        self.charset = config.get('mysql', 'charset')


    # 获取当天爬取数据
    def getRecentCommentData(self, crt_date):
        conn = pymysql.connect(host = self.host, port = int(self.port), 
                user = self.user, password = self.password, db = self.db)
        try:
            cur = conn.cursor()
            # TODO
            sqlStr = 'SELECT * FROM t_product_comments WHERE commentDate >=  "%s"' %(crt_date)
            cur.execute(sqlStr)
            result = cur.fetchall()
            return result
        except Exception as e:
            conn.rollback()
            print(e)
        finally:
            conn.close()
        return ''

    def saveCleanComments(self, item):
        conn = pymysql.connect(host = self.host, port = int(self.port), 
                user = self.user, password = self.password, db = self.db)
        try:
            cur = conn.cursor()
            sqlStr = "INSERT INTO t_cln_product_info (productCode, userName, comments, commentTime, sentiments, commentDate) VALUES('%s', '%s', '%s', '%s', '%s', '%s') \
                " %(item['productCode'], item['user_name'], item['content'], item['comment_time'], item['sentiment'], item['crt_time'])
            cur.execute(sqlStr)
            cur.close()
            conn.commit()
        except Exception as e:
            conn.rollback()
            print(e)
        finally:
            conn.close()

    def checkClnSameComments(self, userName, comments):
        conn = pymysql.connect(host = self.host, port = int(self.port), 
                user = self.user, password = self.password, db = self.db)
        try:
            cur = conn.cursor()
            sqlStr = 'SELECT * FROM t_cln_product_info WHERE userName = "%s" AND comments = "%s" ' %(userName, comments)
            cur.execute(sqlStr)
            result = cur.fetchall()
            if result is not None and len(result) > 0:
                return result[0]
            else:
                return ''
        except Exception as e:
            conn.rollback()
            print(e)
        finally:
            conn.close()
        return ''