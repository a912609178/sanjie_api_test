import os

BASE_PATH = os.path.split(os.path.dirname(os.path.abspath(__file__)))[0]
DATA_PATH = os.path.join(BASE_PATH,'datas')
CONFIG_PATH = os.path.join(BASE_PATH,'config')
COMMAN_PATH = os.path.join(BASE_PATH,'comman')
CASE_PATH = os.path.join(BASE_PATH,'case')
REPORT_PATH = os.path.join(BASE_PATH,'reports')
INTERFACE_CASE_PATH = os.path.join(BASE_PATH,'interface_case')