# -*- coding: utf-8 -*-
# 将icon.ico转换成icon.py
import base64


def Code_IMG():
    open_icon = open("icon.ico", "rb")
    b64str = base64.b64encode(open_icon.read())
    open_icon.close()
    write_data = "img = '%s'" % b64str
    f = open("icon.py", "w+")
    f.write(write_data)
    f.close()


Code_IMG()
