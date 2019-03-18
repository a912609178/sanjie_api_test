from urllib3 import encode_multipart_formdata
import requests
from common.get_token import get_token
t = get_token()
header = {'appKey': '2d99a4c9-93f2-4b51-a058-beebd4a5cba7', 'secret': '6de11e5e-48f3-4bd5-9b02-1fbc9f56da19', 'X-APP-INFO': '{"channel":"APP-GW1-Android-1.0.9","deviceType":"android", "imei":"99001087507262","mac":"Failed","manufacturer":"Xiaomi","model":"MIMAX 2", "os":"7.1.1","version":"1.0.9"}'}
header['Authorization'] = t
def post_files(url, filename, filepath):
    data = {}
    data['file'] = (filename, open(filepath, 'rb').read())
    encode_data = encode_multipart_formdata(data)
    data = encode_data[0]
    header['Content-Type'] = encode_data[1]
    r = requests.post(url, headers=header, data=data)
    print(r.content)
