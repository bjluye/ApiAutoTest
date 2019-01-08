# vi receive_msg.py
 #!/usr/bin/env python
import signal
import pika
#signal.signal(signal.SIGPIPE, signal.SIG_DFL)
signal.signal(signal.SIGINT, signal.SIG_DFL)

credentials = pika.PlainCredentials('omp_test', '!QAZ@WSX')
connection = pika.BlockingConnection(pika.ConnectionParameters(
                                     '10.165.196.104',
                                     5672,
                                     '/omp_test_host',
                                     credentials))
channel = connection.channel()

arguments = {"x-message-ttl":604800000}
channel.queue_declare(queue='p4p_adv_audit_queue.yml',durable='True',arguments=arguments)
body =  {"agentId":1007,
         "agentName":"北京派瑞威行广告有限公司（luye）",
         "channel":2,
         "credentials":[{"cid":1,"isPerpetual":1,"name":"组织机构代码证","relationId":1793,"status":0,"subTime":"2018-11-20 16:55:00","type":1,"urls":["https://pg-ad-b1.ws.126.net/yixiao/110506/c4233781858cff82ee9f45fe00ea1dac.jpg"]},{"cid":26,"expireTime":"2039-01-26","isPerpetual":0,"name":"ICP备案","relationId":1795,"status":0,"subTime":"2018-11-20 16:55:00","type":1,"urls":["https://pg-ad-b1.ws.126.net/yixiao/110506/4c7a46fb1786fea6e23f12adf71cf925.jpg"]},{"cid":25,"expireTime":"2023-01-28","isPerpetual":0,"name":"身份证复印件","relationId":1794,"status":1,"subTime":"2018-11-20 16:55:00","type":1,"urls":["http://pg-ad-b1.nosdn.127.net/yixiao/110506/076e3caed758a1c18c91a0e9cae3368f.jpg"]},{"cid":28,"isPerpetual":0,"name":"1213","relationId":2604,"status":0,"subTime":"2018-11-20 16:55:00","type":0,"urls":["https://pg-ad-b1.ws.126.net/yixiao/110506/51da9ddb036cc76d21f6bbcb204e6f06.jpg"]},{"cid":28,"isPerpetual":0,"name":"tests","relationId":2742,"status":0,"subTime":"2018-11-20 16:55:00","type":0,"urls":["https://pg-ad-b1.ws.126.net/yixiao/110506/51da9ddb036cc76d21f6bbcb204e6f06.jpg"]},{"cid":29,"status":0}],
         "dspId":100000,
         "id":110506,
         "industry":"01",
         "isSensitive":1,
         "name":"一代客户公司",
         "subIndustry":"0102",
         "subTime":"2018-11-20 16:55:00",
         "token":"5bf3cbe40186bd9848c66e10",
         "url":"http://www.sina.com/111111"
         }
def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)
channel.basic_consume(callback,
                      queue='p4p_adv_audit_queue.yml',
                      no_ack=True)
print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()
