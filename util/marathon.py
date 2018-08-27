#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import json
import sys
import pymysql
# 导入日志模块
import logging

charset = 'utf-8'

reload(sys)
sys.setdefaultencoding(charset)

marathon_url = "http://172.20.17.4:8080"

mysql_conn = pymysql.connect(host='localhost', port=3306, user='root', password='19940423', database='marathon')

# 日志模块配置
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s-%(levelname)s : %(message)s')
# logging.basicConfig(filename='/var/log/marathon.log',level=logging.DEBUG,format='%(asctime)s-%(levelname)s:%(message)s')


def get_all_apps():
    request_url = marathon_url + "/v2/apps"
    resp = requests.get(request_url)
    result_code = resp.status_code
    if result_code == 200:
        # 获取所有的应用列表
        rt = json.loads(resp.content, encoding=charset)['apps']
        cursor = mysql_conn.cursor()
        for item in rt:
            app_id = item['id']
            if app_id.startswith('/dcee'):
                app_name = app_id[6:]
                app_json = json.dumps(item)
                sql_str = ("insert into deployment (app_name, app_json) value ('%s', '%s')" % (app_name, app_json))
                #sql_str = "select now();"
                try:
                    cursor.execute(sql_str)
                    mysql_conn.commit()
                    logging.info('插入数据 %s 成功。' % app_name)
                except:
                    mysql_conn.rollback()
                    logging.error('插入数据 %s 错误。' % app_name)
                #finally:
                #    cursor.close()
                #    mysql_conn.close()


if __name__ == '__main__':
    get_all_apps()

