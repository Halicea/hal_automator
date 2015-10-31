import os, sys, json
from flask import Flask
import flask.ext.login as flask_login
from flask.ext.socketio import SocketIO
from hal_configurator.web.attributes import crossdomain

current_dir = os.path.dirname(__file__)
root_dir = os.path.abspath(os.path.join(current_dir, '../../../'))

sys.path.append(root_dir)

app_config = json.loads(open(os.path.join(current_dir, '../config.json'), 'r').read())
workspace_path = os.path.expanduser(app_config['workspace_path'])


app = Flask(__name__, static_folder='./static', static_url_path='')
app.secret_key = 'wergwergfjetwefewf'
socketio = SocketIO(app)

@app.route('/static/<path:filename>')
@crossdomain(origin="*")
@flask_login.login_required
def base_static(filename):
    return send_from_directory(workspace_path, filename)

import auth
import config

