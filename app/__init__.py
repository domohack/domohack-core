# -*- coding: utf-8 -*-

from flask import Flask, render_template
from flask.ext.plugins import PluginManager, get_plugins_list

def create_app(config_name):
    app = Flask(__name__, static_url_path='/static')

    # Initialisation des plugins
    plugin_manager = PluginManager()
    plugin_manager.init_app(app,plugin_folder='plugins')

    @app.route('/')
    def index():
        return render_template("index.html", plugins=get_plugins_list())

    return app
