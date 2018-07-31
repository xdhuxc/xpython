#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import json
import sys

charset = 'utf-8'

reload(sys)
sys.setdefaultencoding(charset)

marathon_url = "http://172.20.17.4:8080"


def get_all_apps():
    request_url = marathon_url + "/v2/apps"
    resp = requests.get(request_url)
    result_code = resp.status_code
    if result_code == 200:
        # 获取所有的应用列表
        rt = json.loads(resp.content, encoding=charset)['apps']
        for item in rt:


            app_id = item['id']
            if app_id.startswith('/dcee'):
                app_name = app_id[6:]
                print('app_id: %s, app_name: %s' % (app_id, app_name))


if __name__ == '__main__':
    print(sys.getdefaultencoding())
    get_all_apps()

