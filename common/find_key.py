data = {'code': 200, 'message': '成功', 'data': {'userId': 447161, 'token': 'eyJhbGciOiJIUzUxMiJ9.eyJqdGkiOiJqd3QiLCJzdWIiOiJ7XCJ1c2VySWRcIjo0NDcxNjEsXCJtb2JpbGVcIjpcIjE4MioqKio5MTgyXCIsXCJzZXNzaW9uSWRcIjpcIjdmMGIwMTEyLTY4NjMtNDhiYS1iN2JjLTM0MGEyYTYxYmQzMFwiLFwiaXNzXCI6XCJvdWRpbmcuY29tXCIsXCJpYXRcIjoxNTUxMTQ4MTYxOTIzLFwiZXhwXCI6MTU1Mzc0MDE2MTkyMyxcInBhc3N3b3JkXCI6bnVsbCxcImJsb2NrZWRcIjpmYWxzZSxcImFsbG93X2V4cFwiOjE1NTM3NDAxNjY5MjN9IiwiYXV0aCI6IlJPTEVfUkVHVUxBUiIsImlhdCI6MTU1MTE0ODE2MSwiZXhwIjoxNTUxMzY0MTYxfQ.lAmgBnMa8XaUtIzshJgKpVlyuSgScl1hZAvawTKoROUK2WetU2Dmt4eObTSNVJGx6e254viLbVBs4Ei8sofK5g', 'userType': '2'}}
find_key = 'data'
find_value = []

def get_more_value(data,*keys):
    for key in keys:
        find_value.append(get_key_node(data,key))

def get_key_node(dict_data,obj_key):
    for key, value in dict_data.items():
        if value:
            if not isinstance(value, dict):
                if key == obj_key:
                    return value
            else:
                return get_key_node(value,obj_key)
a = 'userId'
b = 'token'
get_more_value(data, 'userId', 'token')
print(find_value)