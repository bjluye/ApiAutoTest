#-*- coding:utf-8 -*-
import ConfigParser

class Config :

    def __init__(self,path):
        self.path = path
        self.ini = ConfigParser()
        self.ini.read(self.path)
