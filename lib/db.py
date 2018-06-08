#-*- coding:utf-8 -*-
__author__ = 'luye'
import pymysql
from lib.Config import Config

class MySQL:

    ini = Config('E:\python_code\ApiAutoTest\conf\dataSource.ini')
    dict_item = {}
    list_item = ini.get_item_by_section('mysql')
    for k,v in list_item:
        dict_item[k] = v
    '''
        1、_xxx 不能用于’from module import *’ 以单下划线开头的表示的是protected类型的变量。即保护类型只能允许其本身与子类进行访问。
        2、__xxx 双下划线的表示的是私有类型的变量。只能是允许这个类本身进行访问了。连子类也不可以
        3、__xxx___ 定义的是特列方法。像__init__之类的
    '''
    def connect(self):
        db = pymysql.connect(
            host     = self.dict_item['mysql_host'],
            port     = int(self.dict_item['mysql_port']),
            user     = self.dict_item['mysql_username'],
            password = self.dict_item['mysql_password'],
            database = self.dict_item['mysql_database'],
            charset  = self.dict_item['mysql_charset']
        )
        return db

    # 插入、删除、更新数据，不带参数
    def update(self,sql):
        cursor = self.connect().cursor()
        try:
            cursor.execute(sql)
            self.connect().commit()
        except:
            self.connect().rollback()

    # 插入、删除、更新数据，带参数
    def update(self,sql,params):
        cursor = self.connect().cursor()
        try:
            cursor.execute(sql,params)
            self.connect().commit()
        except:
            self.connect().rollback()

    # 查询数据
    def query(self,sql):
        cursor = self.connect().cursor()
        try:
            cursor.execute(sql)
            result = cursor.fetchall()
        except:
            print("Error: unable to fetch data")
        return result

if __name__ == '__main__':
    mysql = MySQL()
    sql = 'select * from agent_info where id = 1007'
    print(mysql.query(sql))




