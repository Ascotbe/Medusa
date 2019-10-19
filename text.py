import pymysql  #导入 pymysql

db= pymysql.connect(host="localhost",user="root",password="zhouyuchen",db="medusa",port=3306)

# 使用cursor()方法获取操作游标
cur = db.cursor()

sql_insert ="""insert into vulnerability values(4,'liu','1d','12d34','12234','1234','1234')"""


cur.execute(sql_insert)
#提交
db.commit()
