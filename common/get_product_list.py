# from common.get_token import get_token
# import requests
# a = '{"channel":"APP-GW1-Android-1.0.9","deviceType":"android","imei":"99001087507262", \
# "mac":"Failed","manufacturer":"Xiaomi","model":"MI MAX 2","os":"7.1.1","version":"1.0.9"}'
# token = get_token()
# s = requests.session()
# url1 = 'http://192.168.1.162:38112/v2/order/status/step'
# url2 = 'http://192.168.1.162:38112/v2/manage/product/list?page=1&pageSize=20'
# headers = {'Content-Type':'application/json;charset=UTF-8','Authorization':''}
# headers['Authorization'] = token
# result = s.get(url=url1, headers=headers).json()
# print(result)
data = {'code': 200, 'message': '成功', 'data': {'userId': 447161, 'token': 'eyJhbGciOiJIUzUxMiJ9.eyJqdGkiOiJqd3QiLCJzdWIiOiJ7XCJ1c2VySWRcIjo0NDcxNjEsXCJtb2JpbGVcIjpcIjE4MioqKio5MTgyXCIsXCJzZXNzaW9uSWRcIjpcIjYxYThkN2M0LWZkMWItNDgxZS1iNzM4LTk1YjllZWM1OWYzYlwiLFwiaXNzXCI6XCJvdWRpbmcuY29tXCIsXCJpYXRcIjoxNTUxMTAyNDk4NDI5LFwiZXhwXCI6MTU1MzY5NDQ5ODQyOSxcInBhc3N3b3JkXCI6bnVsbCxcImJsb2NrZWRcIjpmYWxzZSxcImFsbG93X2V4cFwiOjE1NTM2OTQ1MDM0Mjl9IiwiYXV0aCI6IlJPTEVfUkVHVUxBUiIsImlhdCI6MTU1MTEwMjQ5OCwiZXhwIjoxNTUxMzE4NDk4fQ.Yi4WK-T6LDhO-5YqcbJS6bprJ_IIDF2cJhPQmhExQLErKYdoO8hkNAgA4ce0yODynjHt9vQVLPh8k0mnrTFbfQ', 'userType': '2'}}


def get_key_node(dict_data,obj_key):
    for key,value in dict_data.items():
        if value:
            if not isinstance(value,dict):
                if key==obj_key:
                    print(value)
                    return value
            else:
                get_key_node(value,obj_key)

get_key_node(data,"userId")
