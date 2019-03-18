# -*- coding: utf-8 -*-
#!usr/bin/python
import unittest, ddt
from common.confighttp import ConfigHttp
from common.case import get_xls
from common.update_ocr import post_files
from common.live import living_body
from common.tel_bk_tb import sql
from common.asset_approval import update_order_530,update_order_600,update_order_850,update_order_900,pay_user_member
#申明类、公共参数
sheet_name = 'ly'
api_xls = get_xls('api_test.xlsx', sheet_name)
LocalConfigHttp = ConfigHttp()


@ddt.ddt
class TestReverse(unittest.TestCase):
    '''初始化'''
    def setParameters(self, case_id, description, interface, headers, method, data, filename, filepath, assert_key, message):
        self.case_id = str(case_id)
        self.description = str(description)
        self.interface = str(interface)
        self.headers = str(headers)
        self.method = str(method)
        self.data = str(data)
        self.filename = filename
        self.filepath = filepath
        self.assert_key = str(assert_key)
        self.message = str(message)

    @classmethod
    def setUpClass(self):
        pass
    @classmethod
    def tearDownClass(self):
        pass
    def setUp(self):
        pass
    def tearDown(self):
        pass




    @ddt.data(*api_xls)
    @ddt.unpack
    def testReverse(self, id, description, interface, headers, method, data, filename, filepath, assert_key, message):
        self.setParameters(id, description, interface, headers, method, data, filename, filepath, assert_key, message)
        if description == 'ocr':
            post_files(url=self.interface, filename=self.filename, filepath=self.filepath)
        elif description == 'sql':
            sql()
        elif description == 'living':
            living_body()
        elif description == 'approve':
            update_order_530()
        elif description == 'order_sign':
            update_order_600()
        elif description == 'order_850':
            update_order_850()
        elif description == 'order_900':
            update_order_900()
        elif description == 'pay_user_member':
            pay_user_member()
        else:
            if data:
                datas = eval(self.data)
            else:
                datas = {}
            print(datas)
            LocalConfigHttp.set_data(datas)
            LocalConfigHttp.set_headers(self.headers)

            api_url = self.interface
            if 'http'in api_url:    #判断url格式是否需要拼接
                LocalConfigHttp.set_url2(api_url)
            else:
                LocalConfigHttp.set_url(api_url)
            if self.method == 'get':
                self.response = LocalConfigHttp.get()
            else:
                self.response = LocalConfigHttp.post()#调接口
            content = self.response.json()
            global assert_value
            assert_value = content[self.assert_key]


    #断言
    def checkResult(self):
        self.assertEqual(assert_value, self.message)




if __name__ == '__main__':
    unittest.main()