#!/usr/bin/env python
# -*- coding: utf-8 -*-

import smtplib
from email.mime.text import MIMEText
from email.header import Header
import os

# http://www.runoob.com/python/python-email.html
#

mail_host = os.getenv('mail_host') or 'smtp.163.com'
mail_user = os.getenv('mail_user') or 'xdhuxc@163.com'
mail_password = os.getenv('mail_password') or 'Xdhuxc@163'
charset = 'utf-8'


mail_message = """
<p> Python 邮件发送测试...</p>

"""
message = MIMEText(mail_message, 'html', charset)
message['From'] = Header('资源报告', charset)
message['To'] = Header('', charset)
