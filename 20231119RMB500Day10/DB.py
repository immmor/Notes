

import pymysql as MySQLdb
# import logging
#
# logger =logging.getLogger(__name__)

# 不是每一个接口都需要执行数据库断言，所有有的接口需要有的接口不需要，所以就是动态执行，要利用热加载
class DBServer:
    def __init__(self, *args, **kwargs):
        self.db = MySQLdb.connect(*args, **kwargs)
        self.c = self.db.cursor()  # 创建新的绘画

    def execute_sql(self, sql):
        self.c.execute(sql)  # 执行sql脚本
        # logging.info(f"{sql=}")
        res = self.c.fetchall()  # 返回多行结果
        # res = self.c.fetchone() # 返回单行结果
        return res


db = DBServer(
    host="127.0.0.1",
    port=3306,
    user="root",
    password="123",
    database="qt"
)

if __name__ == '__main__':
    res = db.execute_sql("select *  from t_student where sname = 'huoshan'")
    print(res)
    print(res[0][1])
    print(type(res[0][1]))
    print(type(res))
    print(db.execute_sql("select * from t_student where age>18"))
