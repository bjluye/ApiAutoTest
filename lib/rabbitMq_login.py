#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pika
from lib.Config import Config
from lib.get_yml import get_yml_data
import json

class rabbitMq_login(object):

    def __init__(self):
        ini = Config('../conf/dataSource.ini')
        dict_item = {}
        list = ini.get_item_by_section('rabbit-mq')
        for k,v in list:
            dict_item[k] = v
        credentials = pika.PlainCredentials(dict_item['username'], dict_item['password']) #注意用户名及密码
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(
                                             dict_item['host'],
                                             dict_item['port'],
                                             dict_item['vhost'],
                                             credentials))

    def connect_mq(self):
        self.channel = self.connection.channel()
        return self.channel

    def p4p_adv_audit_queue(self):
        channel = self.connect_mq()
        tmp = get_yml_data('p4p_adv_audit_queue.yml')
        arguments = {"x-message-ttl":tmp['x-message-ttl']}

        channel.queue_declare(queue=tmp['queue'], durable=tmp['durable'], arguments=arguments)

        body = json.dumps(tmp['body'])
        channel.basic_publish(exchange=tmp['exchange'],
                                   routing_key=tmp['routing_key'],
                                   body=body
                                  )
        print(" [x] Sent 'Hello_World'")
        self.connection.close()


if __name__ == '__main__':
    r = rabbitMq_login()
    #r.connect_mq()
    r.p4p_adv_audit_queue()

