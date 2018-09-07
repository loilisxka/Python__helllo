# -*- coding: utf-8 -*-
import hmac,random#引入需要的模块

def get_md5(key,s):#利用hmac算法获取摘要
    return hmac.new(key.encode('utf-8'),s.encode('utf-8'),'MD5').hexdigest()
#主要目的是输出一个带有随机变量的key，并且摘要
class User(object):
    def __init__(self,usernamem,password):
        self.username = usernamem
        self.key = ''.join([chr(random.randint(48,122))for i in range(20)])
        self.password = get_md5(self.key,password)
db = {
    'micheal':User('micheal','123456'),
    'bob':User('bob','abc999'),
    'alice':User('alice','alice2008')
}
def login(username,password):
    user = db[username]
    return user.password == get_md5(user.key,password)#这里的user.password是类里面的
    # 但是输入到get_md5的key要以随即出来的
#测试
assert login('micheal','123456')
assert login('bob','abc999')
assert login('alice','alice2008')
assert not login('micheal','1234567')
assert not login('bob','123456')
assert not login('alice','Alice2008')
print('ok')