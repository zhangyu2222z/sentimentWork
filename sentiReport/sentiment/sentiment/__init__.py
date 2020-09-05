from __future__ import absolute_import
# 引入MyDjango下的cerely.py
from .myCelery import app as celery_app
# mysql部分
import pymysql

pymysql.version_info=(1,3,13,"final",0)
pymysql.install_as_MySQLdb()

