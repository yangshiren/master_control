import sqlite3


class TrackDb:

    @staticmethod
    def createDB():
        con = sqlite3.connect("master.db")
        # 实例化游标
        cur = con.cursor()
        Sql = '''CREATE TABLE IF NOT EXISTS param_setting_db(
                  plan_id INTEGER            -- 关联方案ID
                  num INTEGER PRIMARY KEY,   -- 编号 
                  circle INTEGER,            -- 圈
                  move TEXT,                 -- 直线/圆弧
                  axis1 INTEGER,             -- 轴1   move为圆弧 x 偏移量
                  axis2 INTEGER,             -- 轴2   move为圆弧 y 偏移量
                  axis3 INTEGER,             -- 轴3  
                  axis4 INTEGER,             -- 轴4
                  axis5 INTEGER,             -- 轴5
                  vel  REAL,                 -- 速度
                  start REAL,                -- 起步
                  brake REAL,                -- 刹车
                  zoom_in REAL,              -- 拉近
                  zoom_out REAL,             -- 拉远
                  pros_cons INTEGER,         -- 顺/逆
                  delay INTEGER,             -- 延迟
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

    @staticmethod
    def findByPlan(plan_id):
        con = sqlite3.connect("master.db")
        # 实例化游标
        cur = con.cursor()
        sql = '''SELECT * FROM param_setting_db WHERE plan_id = ? ORDER BY num ASC '''
        try:
            cur.execute(sql,(plan_id,))
            return cur.fetchall()
        except BaseException as e:
            print(e)
            print("Create failed")
        finally:
            cur.close()
            con.close()