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
mail_password = os.getenv('mail_password') or '952137w'

sender = 'xdhuxc@163.com'
receivers = ['wanghuanf@yonyou.com']
charset = 'utf-8'


mail_message = """
<p> Python 邮件发送测试...</p>

"""
message = MIMEText(mail_message, 'html', charset)
message['From'] = Header('资源报告', charset)
message['To'] = Header('开发运维', charset)

subject = 'Python SMTP 邮件测试'
message['Subject'] = Header(subject, charset)

try:
    smtpObject = smtplib.SMTP('localhost')
    smtpObject.sendmail(sender, receivers, message.as_string())
    print('邮件发送成功')
except:
    print('Error：无法发送邮件。')
