import ClassCongregation
import hashlib
import time
import sqlite3

#a=ClassCongregation.login("123",).logins()
# def hash_code(s, salt='Asc0e6e'):# 加点盐
#     h = hashlib.sha256()
#     s += salt
#     h.update(s.encode())  # update方法只接收bytes类型
#     return h.hexdigest()
#
#
# hash_passwd = hash_code("12311")#加密后写入
# write_presence=ClassCongregation.register('username', hash_passwd, 'emil').register_write()
# def get_session(username):#用来查询数据库中的session
#     h = hashlib.sha256()
#     salt=str(int(time.time()))
#     username += salt
#     h.update(username.encode())
#     print(h.hexdigest())
#
def a():
    print("1")
    return "ccccc"
def b():
    print("2")
    return "aaaa"

def c():
    print("3")
    return "ccsss"

def main():
    lists=[a(),b(),c()]
    for i in lists:
        print(i)


main()