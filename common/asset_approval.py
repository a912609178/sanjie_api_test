from common.sanfang import MyPysql
import time
import requests
from common.confighttp import ConfigHttp

config = ConfigHttp()
t=time.time()
newtime=int(round(t * 1000))

sql = MyPysql()

def update_order_530():
    sql1 = "SELECT id from user_order ORDER BY id DESC LIMIT 1;"
    result = sql.execute(sql1)
    global order_id
    order_id=result[0][2]
    sql2 = "UPDATE user_order SET biz_status = 530,modify_time ="+str(newtime)+",remark = 'dd',approve_time="+str(newtime)+",approve_user = '刘洋',approve_user_gid = 'caf47b1c-8bd3-48ce-b06f-5b1725047c26' WHERE id ="+str(id)
    sql.update(sql2)


def update_order_600():
    sql3 = 'SELECT id from bank_card ORDER BY id DESC LIMIT 1'
    sql1 = "SELECT id from user_order ORDER BY id DESC LIMIT 1;"
    result1 = sql.execute(sql3)
    result = sql.execute(sql1)
    bc_id = result1[0][0]
    order_id = result[0][0]
    sql4 = "UPDATE bank_card SET use_type=1, open_account_state=1 where id="+str(bc_id)
    sql.update(sql4)
    sql2 = "UPDATE user_order SET biz_status = 600 where id ="+str(order_id)
    sql.update(sql2)


def update_order_850():
    # t=get_token()
    # s=requests
    # header = {'appKey': '2d99a4c9-93f2-4b51-a058-beebd4a5cba7', 'secret': '6de11e5e-48f3-4bd5-9b02-1fbc9f56da19',
    #           'X-APP-INFO': '{"channel":"APP-GW1-Android-1.0.9","deviceType":"android", "imei":"99001087507262","mac":"Failed","manufacturer":"Xiaomi","model":"MIMAX 2", "os":"7.1.1","version":"1.0.9"}'}
    # header['Authorization'] = 'eyJhbGciOiJIUzUxMiJ9.eyJqdGkiOiJqd3QiLCJzdWIiOiJ7XCJ1c2VySWRcIjo0NDcyMDcsXCJtb2JpbGVcIjpcIjEzNCoqKio5MjgyXCIsXCJzZXNzaW9uSWRcIjpcIjgzYmY4ZmQyLWM1ODYtNGU0YS05YjE1LTUyYTVlZWM4MDQ4NFwiLFwiaXNzXCI6XCJvdWRpbmcuY29tXCIsXCJpYXRcIjoxNTUyNDc4MjAxNTAxLFwiZXhwXCI6MTU1NTA3MDIwMTUwMSxcInBhc3N3b3JkXCI6bnVsbCxcImJsb2NrZWRcIjpmYWxzZSxcImFsbG93X2V4cFwiOjE1NTUwNzAyMDY1MDF9IiwiYXV0aCI6IlJPTEVfUkVHVUxBUiIsImlhdCI6MTU1MjQ3ODIwMSwiZXhwIjoxNTUyNjk0MjAxfQ.4PW48dD_Yg096z9PnajkzeQWCUFcZUAPV9XFDyiknZnaVwBcvUENy-5LXD7uH1cFxAmvG6oK5lZ3auvc6cawig'
    # url = 'http://192.168.1.162:38112/v2/order/withdrawAuthorization'
    # r = s.get(url=url, headers=header)
    # print(r.cookies)
    # url1=r.json()['data']
    # data = {
    #     'projectNo': 312693482503266304,
    #     'platformProjectName': '水莲金条',
    #     'name': '刘洋',
    #     'password': 123456,
    #     'requestKey': '4b47bc54-cc73-4b52-94e9-df352ddfb871'
    # }
    sql1 = "SELECT id from user_order ORDER BY id DESC LIMIT 1;"
    result1 = sql.execute(sql1)
    order_id = result1[0][0]
    sql2 = "UPDATE user_order SET biz_status = 850 where id =" + str(order_id)
    sql.update(sql2)


def update_order_900():
    sql1 = "SELECT order_sn from user_order ORDER BY id DESC LIMIT 1;"
    result1 = sql.execute(sql1)
    order_id = result1[0][0]
    url = 'https://mock.facebank.cn/test/assetReleCGController?assetId='+str(order_id)+'&rate=6.7'
    r=requests.get(url,verify=False)
    print(r.status_code)
    new = 0
    while new <= 600:
        time.sleep(30)
        new += 30
        url1 = 'http://192.168.1.162:37112/job/orderStatusQuery'
        requests.get(url1)


def pay_user_member():
    t = time.time()
    newtime = int(round(t * 1000))
    sql1 = "SELECT id from order_urge ORDER BY id DESC LIMIT 1;"
    result=sql.execute(sql1)
    id = result[0][0]
    sql2 = "update order_urge SET urge_state = 1, pay_state = 1, urge_end_time="+str(newtime)+" where id="+str(id)
    sql.update(sql2)


def repayment():
    headers = config.set_headers()
    url = 'http://192.168.1.162:38112/v2/repayment/getRepaymentInfo'
    s = requests.session()
    result=s.get(url=url,headers=headers)
    creditRepaymentId= result.json()['data']['creditRepaymentId']
    repaymentlist = result.json()['data']['repaymentList']
    listnum = len(repaymentlist)
    sql3 = 'SELECT id from bank_card ORDER BY id DESC LIMIT 1'
    bc_id = sql.execute(sql3)
    url1 = 'http://192.168.1.162:38112/v2/repayment/request'
    data = {
        "bankCardId": bc_id[0][0],
        "repaymentType": "1",
        "repaymentId": creditRepaymentId
    }
    for i in range(listnum+1):
        if i >0:
            r=s.post(url=url1,headers=headers,json=data)
            print(r)



repayment()