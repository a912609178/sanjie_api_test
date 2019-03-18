import requests
from rediscluster import StrictRedisCluster

mobile = '13430329282'


def send_SMS():
    url = 'http://192.168.1.162:38112/v2/authorize/sendVerifyCode?mobile='
    url1 = url + mobile
    requests.get(url1).json()


def redis_cluster_get_verifyCode():
    send_SMS()
    redis_nodes = [{'host': '192.168.1.162', 'port': 7001},
                   {'host': '192.168.1.162', 'port': 7002},
                   {'host': '192.168.1.162', 'port': 7003},
                   {'host': '192.168.1.162', 'port': 7004},
                   {'host': '192.168.1.162', 'port': 7005}
                   ]
    try:
        rediscoon = StrictRedisCluster(startup_nodes=redis_nodes,decode_responses=True)
    except Exception as e:
        print(e)
    verifyCode = rediscoon.get('SMS_VERIFY_'+mobile)
    if verifyCode:
        return verifyCode


def get_token():
    Code = redis_cluster_get_verifyCode()
    headers = {
        'Content-Type':'application/json;charset=UTF-8',
        'appKey': '2d99a4c9-93f2-4b51-a058-beebd4a5cba7',
        'secret': '6de11e5e-48f3-4bd5-9b02-1fbc9f56da19',
        'X-APP-INFO': '{"channel":"APP-GW1-Android-1.0.9","deviceType":"android", \
"imei":"99001087507262","mac":"Failed","manufacturer":"Xiaomi","model":"MIMAX 2", \
"os":"7.1.1","version":"1.0.9"}'
    }
    json = {
        "address": "北京市朝阳区八里庄路100号靠近中国农业银行(北京英家坟支行)",
        "loginType": 1,
        "country": "中国",
        "longitude": 116.495314,
        "mobile": mobile,
        "city": "北京市",
        "district": "朝阳区",
        "latitude": 39.914617,
        "province": "北京市",
    }
    json['verifyCode'] = int(eval(Code))
    url2 = 'http://192.168.1.162:38112/v2/authorize/login'
    r2 = requests.post(url=url2, headers=headers, json=json)
    token = r2.json()['data']['token']
    return token