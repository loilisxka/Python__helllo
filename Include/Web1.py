# -*- coding: utf-8 -*-
from wsgiref.simple_server import make_server
from Web import application

httpd = make_server('',7000,application)
print('loading...')
httpd.serve_forever()