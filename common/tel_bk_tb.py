import pymysql
host = "192.168.1.162"
user = "liuyang"
password = "liuyang"
database = "ironman-bullion"
port = 3306
db = pymysql.connect(host,user,password,database,port)
cursor = db.cursor()
sql1= "SELECT id from `user` GROUP BY id DESC LIMIT 1"
cursor.execute(sql1)
results = cursor.fetchall()
user_id=results[0][0]
print(user_id)
sql2 = """INSERT INTO `telephone_auth`(`user_id`, `auth_url`, `token`, `status`, `sid`, `tel`, `create_time`, `modify_time`, `create_by`, `modify_by`, `is_delete`) VALUES ("""+str(user_id)+""", 'http://crs-ui.dianhua.cn/auth/base.html?token=d8ed4cc8e3799df6f161e2a8d4153241&callback=http://223.223.203.83:38114/v2/callback/passport/telephoneCallback&redirectUrl=http://callback.jiejiejie.com/v2/callback/passportPage/telephonePage&contactor={"usrId":"140321199406260030","usrPhone":"18235329282","usrName":"刘洋"}', 'd8ed4cc8e3799df6f161e2a8d4153241', 1, 'SID7b685c0ba0e0f6094b1755b0da2f3dc1', '18235329282', 1552212665037, 1552212806790, """+str(user_id)+""", """+str(user_id)+""", b'0')"""
sql = """INSERT INTO `bank_card`(`user_id`, `user_real_name`, `card_no`, `bank_code`, `account_bank_name`, `is_binded`, `bank_mobile`, `create_time`, `is_used`, `is_checked`, `account_type`, `is_auth`, `modify_time`, `is_delete`, `extend`, `use_type`, `open_account_state`, `bound_state`) VALUES ("""+str(user_id)+""", '刘洋', '6227000291010127569', 'CCB', '中国建设银行', b'1', '18235329282', 1551411365142, 0, 1, 0, NULL, 1551411365142, 0, NULL, 2, 0, 1)"""
sql3 = """INSERT INTO `teamscorpion`(`user_id`, `task_id`, `u_id`, `mapping_id`, `type`, `account`, `result`, `message`, `timestamp`, `status`, `create_time`, `modify_time`, `create_by`, `modify_by`, `is_delete`) VALUES ("""+str(user_id)+""", 'fdb76420-2e70-11e9-874b-00163e050342', 'd6f72d614ed34514a39dcf95d580a1bb', '6436407276069424055', 'taobao', 'a814547825', b'1', '登录成功', NULL, 2, 1549939453226, 1549939640142, NULL, NULL, b'0')"""
sql4 = """UPDATE user_authen_info uai set uai.has_operator=1,uai.operator_effect_time=1554795416028,uai.has_taobao=1,uai.taobao_effect_time=1554795416028 WHERE uai.user_id ="""+str(user_id)
sql5 ="UPDATE `user` set mobile=18235329282 WHERE id="+str(user_id)
sqls=[sql2,sql,sql3,sql4]


def sql():
    for i in sqls:
        print(i)
        try:
             cursor.execute(i)
             db.commit()
        except Exception as e:
            print(e)