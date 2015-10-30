import flask.ext.login as flask_login
from hal_configurator.web import sockeio
from hal_configurator.web.routes.auth import login_manager
from hal_configurator.web.attributes import crossdomain

@socketio.on('connect', namespace='/builds')
@crossdomain(origin="*")
def on_connect():
	print('Client connected')
    emit('my response', {'data': 'Connected'})

@socketio.on('disconnect', namespace='/builds')
@crossdomain(origin="*")
@flask_login.login_required
def on_disconnect():
    print('Client disconnected')