# !/usr/bin/python
# -*- coding:utf-8 -*-
__author__:'luye'

import requests
import unittest
from lib.Config import Config
import time
from lib.db import MySQL
from lib.redis_api import RedisApi


class LoginTest(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    ini = Config('E:\python_code\ApiAutoTest\conf\dataSource.ini')
    dict_item = {}
    list = ini.get_item_by_section('omp')
    for k,v in list:
        dict_item[k] = v


    r = requests.session()

    def test_get_auth_code(self):
        mredis = RedisApi()
        url_dvcode = 'http://pre.opm.163.com/user/getAuthCode?random='+str((time.time())*1000)
        response = self.r.get(url_dvcode)
        cookies = response.cookies
        login_user = cookies['loginUser']
        redis_value = str(mredis.get('session:ad.omp.b:{}'.format(login_user)))
        redis_value.find('authCodet\x00\x04')
        auth_code = redis_value[-6:-2]
        print(auth_code)
        return auth_code

    def test_omp_login(self):

        data = {
            'name': self.dict_item['name'],
            'password': self.dict_item['password'],
            'authCode': self.test_get_auth_code()
        }
        print(data)
        url_login = 'http://pre.opm.163.com/user/login'
        response = self.r.post(url_login,data)
        print(response.text)

    # def test_agent_login(self):
    #     url_login = "http://pre.p4p.pangu.163.com/agent/login"
    #     mail = self.dict_item['mail']
    #     password = self.dict_item['password']
    #     print(password)
    #     data = {
    #         'mail': mail,
    #         'password': password,
    #         'dvCode': self.get_auth_code()
    #     }
    #     response = self.r.post(url_login,data=data)
    #     print(response.text)


if __name__ == '__main__':
    unittest.main()
    login = LoginTest()
    login.test_get_auth_code()







