# -*- coding: utf-8 -*-
from flask import Blueprint
from app.AppPlugin import AppPlugin

__plugin__ = "FooPlugin"


foo = Blueprint("foo", __name__, template_folder="templates")

class FooPlugin(AppPlugin):

    def setup(self):
        self.register_blueprint(foo, url_prefix="/foo")


