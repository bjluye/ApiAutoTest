#-*- coding:utf-8 -*-
from configparser import ConfigParser
import os
class Config :

    def __init__(self,path):
        #获取当前文件路径
        pwd = os.getcwd()
        #print(pwd)
        # 获取当前文件父路径
        father_pwd = os.path.abspath(os.path.dirname(pwd)+os.path.sep+".")
        #print(father_pwd)

        self.path = path
        self.ini = ConfigParser()
        self.ini.read(self.path)

    # 获取sections列表
    def get_section(self):
        return self.ini.sections()

    # 获取指定的sections的options列表
    def get_options_by_section(self,section):
        return self.ini.options(section)

    # 获取指定section的配置信息列表
    def get_item_by_section(self,section):
        return self.ini.items(section)

    '''
    按类型读取配置信息
    '''

    # 返回字符串类型
    def get_string(self,section,option):
        return self.ini.get(section,option)

    # 返回int类型
    def get_int(self,section,option):
        return self.ini.getint(section,option)

    # 返回float类型
    def get_float(self,section,option):
        return self.ini.getfloat(section,option)

    # 返回bool类型
    def get_bool(self,section,option):
        return self.ini.getboolean(section,option)

    # 新增section
    def add_section(self,section):
        self.ini.add_section(section)
        self.ini.write(open(self.path,"w"))

    # 设置指定option值
    def set_option(self,section,option,value):
        self.ini.set(section,option,value)
        self.ini.write(open(self.path,"w"))

    # 删除指定section
    def del_section(self,section):
        self.ini.remove_section(section)
        self.ini.write(open(self.path, "w"))

    #删除指定option
    def del_optinon(self,section,option):
        self.ini.remove_option(section,option)
        self.ini.write(open(self.path),"w")

if __name__ == "__main__":
    ini = Config('E:\python_code\ApiAutoTest\conf\dataSource.ini')

    #print (ini.get_section())
    #print (ini.get_options_by_section('mysql'))
    print (ini.get_item_by_section('mysql'))
    # 类型为list
    #print(type(ini.get_item_by_section('mysql')))

    # list_item = ini.get_item_by_section('mysql')
    # dict_item = {}
    # for k,v in list_item:
    #     print(k,v)
    #     dict_item[k] = v
    # print(dict_item)











