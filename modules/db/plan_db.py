import sqlite3


class PlanDb:

    @staticmethod
    def createDB():
        con = sqlite3.connect("master.db")
        # 实例化游标
        cur = con.cursor()
        Sql = '''CREATE TABLE IF NOT EXISTS plan_db(
                  id INTEGER PRIMARY KEY AUTOINCREMENT,    -- ID
                  name TEXT  NOT NULL,                     -- 方案名称 
                  is_default INTEGER NOT NULL)             -- 是否默认
              '''
        try:
            cur.execute(Sql)
        except BaseException as e:
            print(e)
            print("Create failed")
        finally:
            cur.close()
            con.close()

    @staticmethod
    def findAll():
        con = sqlite3.connect("master.db")
        # 实例化游标
        cur = con.cursor()
        sql = '''SELECT * FROM plan_db
        '''
        try:
            cur.execute(sql)
            return cur.fetchall()
        except BaseException as e:
            print(e)
            print("Create failed")
        finally:
            cur.close()
            con.close()