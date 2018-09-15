import pymysql
import sys
class mysql_bean:


    def __init__(self,l):
        config = {
            'host': '127.0.0.1',
            'port': 3306,
            'user': 'root',
            'password': 'sxd5a5dwg',
            'db': 'lifeblog',
            'charset': 'utf8',
            'cursorclass': pymysql.cursors.DictCursor,
        }
        self.config =config
        self.l=l

    def open_db(self):
        db = pymysql.connect(**self.config)
        self.db = db
        self.cursor = db.cursor()
        db.set_charset('utf8')

    def close_db(self):

        self.db.close()

    def sql_act(self,sql_str):
        print(sql_str)
        try:
            with self.db.cursor() as cursor:
                # 执行sql语句，插入记录
                self.cursor.execute(sql_str)
                # 没有设置默认自动提交，需要主动提交，以保存所执行的语句
                self.db.commit()
        except:
            t, v, tb = sys.exc_info()
            print(t, v)

    def sql_query(self,sql_str):
        print(sql_str)
        try:
            result = self.db.query(sql_str)
            return result;
        except:
            t, v, tb = sys.exc_info()
            print(t, v)


