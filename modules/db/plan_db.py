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
                  is_default INTEGER NOT NULL)             -- 是否默认  1. 默认
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
        sql = '''SELECT * FROM plan_db'''
        try:
            cur.execute(sql)
            return cur.fetchall()
        except BaseException as e:
            print(e)
        finally:
            cur.close()
            con.close()

    @staticmethod
    def insertDb(name:str,default):
        con = sqlite3.connect("master.db")
        # 实例化游标
        cur = con.cursor()
        sql = '''INSERT INTO plan_db(name, is_default)values(?,?)'''
        try:
            cur.execute(sql, (name, default))
            inserted_id = cur.lastrowid
            con.commit()
            return inserted_id
        except BaseException as e:
            print(e)
        finally:
            cur.close()
            con.close()
        return -1

    @staticmethod
    def updateAllDefault():
        con = sqlite3.connect("master.db")
        # 实例化游标
        cur = con.cursor()
        sql = ''' UPDATE plan_db SET is_default = ? WHERE 1=1'''
        try:
            cur.execute(sql, (0,))
            inserted_id = cur.lastrowid
            con.commit()
            return inserted_id
        except BaseException as e:
            print(e)
        finally:
            cur.close()
            con.close()

    @staticmethod
    def findByName(name:str):
        con = sqlite3.connect("master.db")
        # 实例化游标
        cur = con.cursor()
        sql = '''SELECT * FROM plan_db WHERE name = ?'''
        try:
            cur.execute(sql,(name,))
            return cur.fetchall()
        except BaseException as e:
            print(e)
        finally:
            cur.close()
            con.close()