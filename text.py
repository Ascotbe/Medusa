import ClassCongregation
import hashlib
#ClassCongregation.register("13333","dsadsd","1@qq.com").register_write()
#print(ClassCongregation.VulnerabilityInquire("5").Inquire())
#a=ClassCongregation.register("123","dsadsd","1@qq.com").register_inquire_user()
#a=ClassCongregation.login("123",).logins()
def hash_code(s, salt='Asc0e6e'):# 加点盐
    h = hashlib.sha256()
    s += salt
    h.update(s.encode())  # update方法只接收bytes类型
    return h.hexdigest()


hash_passwd = hash_code("12311")#加密后写入
write_presence=ClassCongregation.register('username', hash_passwd, 'emil').register_write()