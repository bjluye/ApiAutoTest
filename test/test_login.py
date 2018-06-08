# !/usr/bin/python
# -*- coding:utf-8 -*-
__author__:'luye'

import requests
import unittest
from lib.Config import Config
from lib.db import MySQL
from lib.redis_api import RedisApi


class LoginTest(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    ini = Config('E:\python_code\ApiAutoTest\conf\dataSource.ini')
    dict_item = {}
    list = ini.get_item_by_section('agent')
    for k,v in list:
        dict_item[k] = v


    r = requests.session()

    def get_auth_code(self):
        url_dvcode = "http://pre.p4p.pangu.163.com/common/getDvCode"
        response = self.r.get(url_dvcode)
        device_id = response.cookies['DEVICE_ID']
        mredis = RedisApi()
        auth_code = mredis.get('p4p:dvCode:{}'.format(device_id))
        return auth_code

    def test_agent_login(self):
        url_login = "http://pre.p4p.pangu.163.com/agent/login"
        mail = self.dict_item['mail']
        password = self.dict_item['password']
        print(password)
        data = {
            'mail': mail,
            'password': password,
            'dvCode': self.get_auth_code()
        }
        response = self.r.post(url_login,data=data)
        print(response.text)


if __name__ == '__main__':
    unittest.main()






