#-*- coding:utf-8 -*-
from configparser import ConfigParser

class Config :

    def __init__(self,path):
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






