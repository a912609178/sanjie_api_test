import os
from xlrd import open_workbook
from common.file_path import DATA_PATH

'''
调用方法获取excel文件中case
返回的数据存入xls数组中
'''

def get_xls(xls_name,sheet_name):
    xls = []
    xlspath = os.path.join(DATA_PATH, 'excel', xls_name)  #获取文件的路径
    file = open_workbook(xlspath)
    sheet = file.sheet_by_name(sheet_name)    #通过sheet名称取数据
    nrows = sheet.nrows   #sheet的行数
    for i in range(nrows):
        if sheet.row_values(i)[0] != 'case_id':
            xls.append(sheet.row_values(i))

    return xls    #将xls的这个变量返回给其他需要调用的地方



if __name__ == '__main__':
    api_xls = get_xls('api_test.xlsx', 'ly')
    print(api_xls)
