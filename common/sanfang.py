import pymysql
class MyPysql:
    def __init__(self):
        self.host = '192.168.1.162'
        self.user = 'liuyang'
        self.password = 'liuyang'
        self.db = 'ironman-bullion'
        self.port = 3306
        # self.sql = None
        self.conn = None
        self.cursor =None

    def get_con(self):
        try:
            self.conn = pymysql.connect(self.host, self.user, self.password,
                                        self.db, self.port, charset='utf8')
        except Exception as e:
            print('连接数据库出错%s' % e)
            return False
        self.cursor = self.conn.cursor()
        return True

    def close(self):
        # 如果数据打开，则关闭；否则没有操作
        if self.conn and self.cursor:
            self.cursor.close()
            self.conn.close()
        return True

    def execute(self, sql, params=None):
        self.get_con()
        try:
            if self.conn and self.cursor:
                self.cursor.execute(sql,params)
                results = self.cursor.fetchall()
                return results
        except Exception as e:
            print("错误%s" %e)

    def insert(self, sql, params=None):
        self.get_con()
        try:
            if self.conn and self.cursor:
                self.cursor.execute(sql,params)
                self.conn.commit()
                self.cursor.close()
                self.conn.close()
        except Exception as e:
            print("错误%s" %e)

    def update(self, sql, params=None):
        self.get_con()
        try:
            if self.conn and self.cursor:
                self.cursor.execute(sql, params)
                self.conn.commit()
                self.cursor.close()
                self.conn.close()
        except Exception as e:
            print("错误%s" % e)

    def delete(self, sql, params=None):
        self.get_con()
        try:
            if self.conn and self.cursor:
                self.cursor.execute(sql, params)
                self.conn.commit()
                self.cursor.close()
                self.conn.close()
        except Exception as e:
            print("错误%s" % e)

if __name__ == "__main__":
    host = "192.168.1.162"
    user = "liuyang"
    password = "liuyang"
    database = "ironman-bullion"
    port = 3306
    sql1 = "SELECT id from `user` ORDER BY id desc LIMIT 1;"

    mysql = MyPysql(host=host,user=user,password=password,
                    db=database,port=port)

    a = mysql.execute(sql1)
    for i in a:
        print(i[0])
