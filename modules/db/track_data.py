import sqlite3

from PySide6.QtSql import QSqlDatabase, QSqlQuery


class TrackData:

    @staticmethod
    def createDB():
        con = sqlite3.connect("track.db")
        # 实例化游标
        cur = con.cursor()
        Sql = '''CREATE TABLE IF NOT EXISTS param_setting_db(
                  num INTEGER PRIMARY KEY,   -- 编号 
                  circle INTEGER,            -- 圈
                  move TEXT,                 -- 直线/圆弧
                  x_val INTEGER,             -- x 偏移量
                  y_val INTEGER,             -- y 偏移量
                  delay INTEGER,             -- 延迟
                  axis1 INTEGER,             -- 轴1
                  axis2 INTEGER,             -- 轴2
                  axis3 INTEGER,             -- 轴3
                  axis4 INTEGER,             -- 轴4
                  axis5 INTEGER,             -- 轴5
                  pros_cons INTEGER,         -- 顺/逆
                  vel  REAL,                 -- 速度
                  start REAL,                -- 起步
                  brake REAL,                -- 刹车
                  zoom_in REAL,              -- 拉近
                  zoom_out REAL,             -- 拉远
                  take_time REAL,            -- 用时
                  organ INTEGER)             -- 机关
              '''
        try:
            cur.execute(Sql)
        except BaseException as e:
            print(e)
            print("Create failed")
        finally:
            cur.close()
            con.close()