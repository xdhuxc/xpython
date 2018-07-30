#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import json

marathon_url = "http://172.20.17.4:8080"


def get_all_apps():
    request_url = marathon_url + "/v2/apps"
    resp = requests.get(request_url)
    apps = j


