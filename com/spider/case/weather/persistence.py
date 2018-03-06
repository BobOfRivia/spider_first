import sys
# 数据持久化层
class data_oper:

    def save_db(self,dataDict):
        from com.spider.database.mysqlcon import mysql_bean
        try:
            mysql_bean = mysql_bean(1)
            mysql_bean.open_db()
            sql="insert into ("
        except:
            t, v, tb = sys.exc_info()
            print(t, v)
        mysql_bean.close_db()


if __name__ == "__main__":
    sourcePath = "../../source/weather/province";
    with open(sourcePath,'rb') as f:
        for line in f.readlines():
            line.split("||")[1];
