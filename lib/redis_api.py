#-*-coding:utf-8-*-
import redis
from lib.Config import Config

class RedisApi:

    ini = Config('E:\python_code\ApiAutoTest\conf\dataSource.ini')
    dict_item = {}
    list_item = ini.get_item_by_section('redis')
    print (list_item)
    for k,v in list_item:
        dict_item[k] = v

    def __init__(self):
        host = self.dict_item['redis_host']
        port = self.dict_item['redis_port']
        password = self.dict_item['redis_password']
        self.pool = redis.ConnectionPool(
            host = host,
            port = port,
            password = password
        )

    def connect(self):
        self.redis = redis.Redis(connection_pool=self.pool)
        return self.redis

    def disconnect(self):
        return self.pool.disconnect()

    '''
    String 操作
    '''
    # 在redis中设置值
    def set(self,key,value,ttl=None):
        if not isinstance(key,str):
            print ("the type of key is not string")
        self.redis.set(key,value,ttl)

    # 获取值
    def get(self,key):
        if not isinstance(key,str):
            print ("the type of key is not string")
        if not self.connect().exists(key):
            print ("the key is not exists")
        val = self.redis.get(key)
        return val

    # 批量设置值
    def mset(self,**kwags):

        self.redis.mset(**kwags)

    # 批量获取值
    def mget(self,keys):
        self.redis.mget(keys)

    # 设置新值，打印原值
    def getset(self,key,value):
        if not isinstance(key,str):
            print ("the type of key is not string")
        old_value = self.redis.getset(key,value)
        return old_value

    # 根据字节获取子序列
    def getrange(self,key,start,end):
        if not isinstance(key,str):
            print ("the type of key is not string")
        self.redis.getrange(key,start,end)

    def keys(self):
        flag = self.connect().keys()
        return flag

    '''
    Hash操作
    '''
    # 根据key获取value
    def hget(self,name,key):
        if not isinstance(name,str):
            print ("the type of key is not string")
        if not self.redis.exists(name):
            print ("the name is not exists")
        val = self.redis.hget(name,key)
        return val

if __name__ == '__main__':
    mredis = RedisApi()
    #pass
    #print(mredis.keys())
    #mredis.keys('ad.p4p.account.target')
    #print(mredis.get('049f674dec6b227f1120fcd2dedeea5f'))
    #print(mredis.hget('ad.job.reg','job-executor@10.165.196.68:9998'))

