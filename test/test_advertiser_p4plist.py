# !/usr/bin/python
# -*- coding:utf-8 -*-
author = '__luye__'

import requests
import unittest
from test.test_login import LoginTest
from lib.get_yml import get_yml_data
import json
from  lib.base import Base
class Adv_P4plist(unittest.TestCase):
    tmp = get_yml_data('test_advertiser_p4plist.yml')
    session = requests.session()

    def get_session(self):
        return self.session

    def setUp(self):
        login = LoginTest()
        print(login)
        self.token,self.cookies = login.omp_login()
        print("!!!!")
        print(self.cookies)
        if self.cookies.get('token') is not None:
            print('success')
        else:
            print('false')

    def tearDown(self):
        pass

    def test_case_1(self):
        payload = self.tmp['case_1']['data']
        data = json.dumps(payload)
        print(type(data))
        headers = {
            'Accept':'application/json, text/plain, */*',
            'Accept-Encoding':'gzip, deflate',
            'Connection':'keep-alive',
            'Content-Length':'108',
            'Content-Type':'application/json;charset=UTF-8',
            'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
            'Cookie':'_ntes_nuid=488d4b75fb9d61c0d885af1cb5b0e990; mail_psc_fingerprint=05e0da35fb604a3f9597a832fad2526a; vjuids=c3089fefc.15d1ab2145e.0.e00ec7fe9ce5e; __gads=ID=2a6af21f6ef64eea:T=1502255560:S=ALNI_MbdV-GUNd8-6uHw9j-cEC3xjRjteQ; mp_MA-B4F3-F90DDC5B7D3B_hubble=%7B%22deviceUdid%22%3A%20%229c8bf334-e741-48f1-afeb-d2050c5ab2d4%22%2C%22updatedTime%22%3A%201506736854382%2C%22sessionStartTime%22%3A%201506736854383%2C%22sessionReferrer%22%3A%20%22https%3A%2F%2Fwww.google.com.hk%2F%22%2C%22sessionUuid%22%3A%20%229d934463-5be4-4879-8314-94d7f58928bf%22%2C%22%24search_engine%22%3A%20%22google%22%2C%22initial_referrer%22%3A%20%22https%3A%2F%2Fwww.google.com.hk%2F%22%2C%22initial_referring_domain%22%3A%20%22www.google.com.hk%22%2C%22persistedTime%22%3A%201506736854383%2C%22LASTEVENT%22%3A%20%7B%22eventId%22%3A%20%22da_screen%22%2C%22time%22%3A%201506736854407%7D%7D; nts_mail_user=luye9224@163.com:-1:1; mp_MA-9506-0E9D982F1392_hubble=%7B%22sessionReferrer%22%3A%20%22%22%2C%22updatedTime%22%3A%201516173128804%2C%22sessionStartTime%22%3A%201516172884957%2C%22deviceUdid%22%3A%20%22c4467331-80d8-4a94-8867-b27e938332c9%22%2C%22initial_referrer%22%3A%20%22%24direct%22%2C%22initial_referring_domain%22%3A%20%22%24direct%22%2C%22persistedTime%22%3A%201516172884949%2C%22LASTEVENT%22%3A%20%7B%22eventId%22%3A%20%22da_u_logout%22%2C%22time%22%3A%201516173128804%7D%2C%22sessionUuid%22%3A%20%22752a99a0-8510-40ae-8593-a2db6d8f06df%22%7D; _ntes_nnid=394a0fa6cce49b964118467227eb8cee,1527489773821; vjlast=1499391465.1529391110.22; vinfo_n_f_l_n3=9ad0ea8042823798.1.6.1499391464557.1517222045217.1529391166510; usertrack=ezq0plswTN6XGTfRqhQQAg==; P_INFO=luye9224@163.com|1533882103|1|kaola|00&99|bej&1531922371&yanxuan#bej&null#10#0#0|&0||luye9224@163.com; NTES_PASSPORT=OGq9i0jamGKcEYO2s.EU6PC7GQLXe7zcAO_J8aoh1ZOUhziQhoRng7uI3rt3PvqGmVZ_JqvHMe85zh2J2efkKQJ6HUDNB3LWe56T_voZFiz7dFg_UK6an6N_CUwfq_zcFI7c_VexAUnFQwNkHzdgwhqEqtWorVTWUZKtrY9iYqHIJ3qeXSgH8OQsn; KAOLA_ACC=luye9224@163.com; __f_=1536747567575; _ga=GA1.2.325148927.1496835198; Province=010; City=010; NNSSPID=3f98d925d5b9426f9a9faa40d438eb3b; NTES_hp_textlink1=old; loginUser=fa406574-bb93-4c4e-9378-b873120cacce; name=admin; passwordadmin'
        }

        if self.cookies.get('token') is not None:
            print('success')
            print(self.cookies.get('token'))
            url = 'http://qa.omp.pangu.163.com/advertiser/p4pList?token=' + self.token
            print(url)

            response = self.session.post(url, data=data, headers=headers)
            print(response.headers)
            print(response.text)
        else:
            print('false')






if __name__ == '__main__':
    unittest.main()