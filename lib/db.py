
import pymysql

class MySQL:

    config = {
        'host': host
    }
    def __init__(self):
        pass

    '''
        1、_xxx 不能用于’from module import *’ 以单下划线开头的表示的是protected类型的变量。即保护类型只能允许其本身与子类进行访问。
        2、__xxx 双下划线的表示的是私有类型的变量。只能是允许这个类本身进行访问了。连子类也不可以
        3、__xxx___ 定义的是特列方法。像__init__之类的
    '''
    def __connect(self):
        pymysql.connect()
