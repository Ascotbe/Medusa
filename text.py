import sqlite3

#如果数据库不存在的话，将会自动创建一个 数据库
con=sqlite3.connect("Medusa.db")
#获取所创建数据的游标
cur=con.cursor()
#创建表
try:
    cur.execute("CREATE TABLE Medusa\
                (id INTEGER PRIMARY KEY,\
                name TEXT NOT NULL,\
                affects TEXT NOT NULL,\
                rank TEXT NOT NULL,\
                suggest TEXT NOT NULL,\
                desc_content TEXT NOT NULL,\
                details TEXT NOT NULL)")
except:
    pass

cur.execute("INSERT INTO Medusa (id,name,affects,rank,suggest,desc_content,details) \
   VALUES (1, 'Paul', 'P222aul', 'California', 'Pauldsds', 'P444dsds' , 'Paucxzasdasddsds');")
#执行完语句需要提交才算结束
con.commit()