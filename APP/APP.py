# -*- coding: utf-8 -*-
# @Time : 2020/2/6
# @Author : zhang
# @Site :
# @File : APP.py
# @Software: PyCharm
from flask import Flask

from APP.functions import init_ext, codeGenerator
from APP.regist import regist
from APP.settings import templates_dir, static_dir


def create_app(config):
    app = Flask(__name__, template_folder=templates_dir, static_folder=static_dir)
    app.config.from_object(config)
    init_ext(app)
    regist(codeGenerator)
    return app