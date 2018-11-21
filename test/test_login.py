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

    ini = Config('..\conf\dataSource.ini')
    dict_item = {}
    list = ini.get_item_by_section('omp')
    for k,v in list:
        dict_item[k] = v

    r = requests.session()

    def get_auth_code(self):
        mredis = RedisApi()
        url_dvcode = 'http://qa.omp.pangu.163.com/user/getAuthCode?random='+str((time.time())*1000)
        response = self.r.get(url_dvcode)
        cookies = response.cookies
        login_user = cookies['loginUser']
        redis_value = str(mredis.get('session:ad.omp.b:{}'.format(login_user)))
        redis_value.find('authCodet\x00\x04')
        auth_code = redis_value[-6:-2]
        return auth_code

    def test_omp_login(self):
        data = {
            'name': self.dict_item['name'],
            'password': self.dict_item['password'],
            'authCode': self.get_auth_code()
        }
        url_login = 'http://qa.omp.pangu.163.com/user/login'
        response = self.r.post(url_login,data)
        if (response.json()['rs'] != 1):
            print("login is failed")

        # 获取用户token
        url_info = 'http://qa.omp.pangu.163.com/user/userInfo'
        payload = {'token':'undefined'}
        response_info = self.r.post(url=url_info,data=payload)
        print(response_info.text)
        if(response_info.json()['rs']!=1):
            print('未能获取用户登录信息')
        print('==================')
        token = response_info.json()['user']['token']
        return token



if __name__ == '__main__':
    unittest.main()
    login = LoginTest()
    login.test_get_auth_code()







