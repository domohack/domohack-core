# -*- coding: utf-8 -*-
from flask import current_app
from flask_plugins import Plugin

class AppPlugin(Plugin):

    def register_blueprint(self, blueprint, **kwargs):
        current_app.register_blueprint(blueprint, **kwargs)


