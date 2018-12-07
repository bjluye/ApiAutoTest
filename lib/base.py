# !/usr/bin/python
# -*- coding:utf-8 -*-
author = '__luye__'
import requests
import unittest
from lib.Config import Config


class Base(object):

    def get_config(self,key):
        ini = Config('..\conf\dataSource.ini')
        dict_item = {}
        list = ini.get_item_by_section(key)
        for k, v in list:
            dict_item[k] = v
        return dict_item

    def add_cookie(self,cookie):
        if not cookie:
            print("COOKIE IS NULL")
            return False
        else:
            requests.utils.add_dict_to_cookiejar()
        return self.session

    def omp_login(self):
        authCode,login_user = self.get_auth_code()
        data = {
            'name': self.dict_item['name'],
            'password': self.dict_item['password'],
            'authCode': authCode
        }
        cookie = {'name': data['name'], 'loginUser': login_user}
        requests.utils.add_dict_to_cookiejar(self.r.cookies,cookie)
        print("_++++++")
        print(self.r.cookies)
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
        print(requests.utils.add_dict_to_cookiejar(self.r.cookies,{'token':token}))
        return token,self.r.cookies

    def p4pList_api_method(self):
        url = '{}/advertiser/p4pList?token='.format(self.get_config('env')['omp_qa'])
        print(url)



if __name__ == '__main__':
    base = Base()
    base.p4pList_api_method()