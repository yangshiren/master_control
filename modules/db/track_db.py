import sqlite3


class TrackDb:

    @staticmethod
    def createDB():
        con = sqlite3.connect("master.db")
        # 实例化游标
        cur = con.cursor()
        Sql = '''CREATE TABLE IF NOT EXISTS param_setting_db(
                  num INTEGER,   -- 编号   顺序
                  plan_id INTEGER,            -- 关联方案ID
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
        finally:
            cur.close()
            con.close()

    @staticmethod
    def findByPlan(plan_id):
        con = sqlite3.connect("master.db")
        cur = con.cursor()
        sql = '''SELECT * FROM param_setting_db WHERE plan_id = ? ORDER BY num ASC '''
        try:
            cur.execute(sql,(plan_id,))
            return cur.fetchall()
        except BaseException as e:
            print(e)
        finally:
            cur.close()
            con.close()

    @staticmethod
    def insertDb(model:dict):
        con = sqlite3.connect("master.db")
        cur = con.cursor()
        sql = '''INSERT INTO param_setting_db(num,plan_id,circle,move, axis1,axis2,axis3,axis4,axis5 ,
                  vel,start,brake,zoom_in,zoom_out,pros_cons,delay,take_time,organ)values(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)'''
        try:
            cur.execute(sql, (model["num"],model["plan_id"],model["circle"],model["move"],model["axis1"],model["axis2"],
                                        model["axis3"],model["axis4"],model["axis5"],model["vel"],model["start"],model["brake"],
                                        model["zoom_in"],model["zoom_out"],model["pros_cons"],model["delay"],model["take_time"],model["organ"]))
            inserted_id = cur.lastrowid
            con.commit()
            return inserted_id
        except BaseException as e:
            print(e)
        finally:
            cur.close()
            con.close()

    @staticmethod
    def deleteDB(plan_id:int):
        con = sqlite3.connect("master.db")
        cur = con.cursor()
        sql = '''DELETE FROM param_setting_db WHERE plan_id = ?;'''
        try:
            cur.execute(sql,(plan_id,))
            con.commit()
        except BaseException as e:
            print(e)
        finally:
            cur.close()
            con.close()
