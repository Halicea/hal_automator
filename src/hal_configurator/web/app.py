from flask import (
    Flask, request, Response, send_from_directory, jsonify,
    send_file, abort)  # @UnusedImport
from hal_configurator.job_server import execute_job
from flask.ext.socketio import SocketIO
from attributes import crossdomain

import os
import json
import sys

current_dir = os.path.dirname(__file__)
root_dir = os.path.abspath(os.path.join(current_dir, '../../'))
sys.path.append(root_dir)

from hal_configurator.lib.config_loaders import FileConfigLoader
from hal_configurator.lib.workspace_manager import Workspace
from hal_configurator.lib.app_configurator import AppConfigurator
from hal_configurator.lib.logers import ConsoleLoger, FileLoger, StringLoger, CompositeLoger


app_config = json.loads(open(os.path.join(current_dir, 'config.json'), 'r').read())
workspace_path = os.path.expanduser(app_config['workspace_path'])
app = Flask(__name__, static_folder='./static', static_url_path='')
socketio = SocketIO(app)

@app.route('/')
@crossdomain(origin="*")
def root():
  return app.send_static_file('index.html')

@app.route("/config")
def list_configs():
  res = [x for x in os.listdir(workspace_path)
         if os.path.isdir(os.path.join(workspace_path, x)) and
         not (x.startswith('.') or x.startswith('_'))]
  return Response(response=json.dumps(res), status=200, mimetype="application/json")

@app.route("/config/jobs")
@crossdomain(origin="*")
def get_jobs_list():
  root = os.path.join(workspace_path, 'jobs')
  res = [x for x in os.listdir(root)
         if os.path.isfile(os.path.join(root, x)) and x.endswith('.halc') and
          not ('_vars' in x or '_ress' in x) and
          not (x.startswith('.') or x.startswith('_'))]
  return Response(response=json.dumps(res), status=200, mimetype="application/json")

@app.route("/config/<environment>")
@crossdomain(origin="*")
def list_environments(environment):
  root = os.path.join(workspace_path, environment)
  res = [x for x in os.listdir(root)
         if os.path.isdir(os.path.join(root, x)) and
          not (x.startswith('.') or x.startswith('_'))]
  return Response(response=json.dumps(res), status=200, mimetype="application/json")


@app.route("/config/<environment>/<name>")
@crossdomain(origin="*")
def list_environment_jobs(environment, name):
  root = os.path.join(workspace_path, environment, name)
  res = [x for x in os.listdir(root)
         if os.path.isfile(os.path.join(root, x)) and x.endswith('.halc') and
          not (x.startswith('.') or x.startswith('_'))]
  return Response(response=json.dumps(res), status=200, mimetype="application/json")


@app.route("/config/<identifier>/<platform>/<name>")
@crossdomain(origin="*")
def get_config(identifier, platform, name):
  filepath = os.path.join(workspace_path, identifier, platform, name)
  conf = FileConfigLoader(filepath).dictionary
  admin = request.args.get('admin')
  result = conf['Variables']
  if bool(admin):
    result = conf
  return Response(response=json.dumps(result), status=200, mimetype="application/json")


@app.route("/config/<identifier>/<platform>/<name>/job/start")
@crossdomain(origin="*")
def job_start(identifier, platform, name):
  Workspace.set(workspace_path)
  filepath = os.path.join(workspace_path, identifier, platform, name)
  loader = FileConfigLoader(filepath)
  config = loader.dictionary
  c_loger = ConsoleLoger()
  s_loger = StringLoger()
  composite_log = CompositeLoger(*[c_loger, s_loger])
  builder = AppConfigurator(loader, composite_log)
  job_output = "No Response"
  try:
    job_output = execute_job.delay(builder, workspace_path, workspace_path).get(100)
  except OSError, e:
    job_output = e.strerror
    job_output+='\nTraceback'+job_output.traceback
  except Exception, e:
    job_output = e.message
    job_output+='\nTraceback'+job_output.traceback
  
  finally:
    res =  Response(response=job_output, status=200, mimetype="text/plain")
    return res
  
@app.route("/config/<identifier>/<platform>/<name>/run")
@crossdomain(origin="*")
def run_config(identifier, platform, name):
  Workspace.set(workspace_path)
  filepath = os.path.join(workspace_path, identifier, platform, name)
  loader = FileConfigLoader(filepath)
  config = loader.dictionary
  c_loger = ConsoleLoger()
  s_loger = StringLoger()
  composite_log = CompositeLoger(*[c_loger, s_loger])
  builder = AppConfigurator(loader, composite_log)
  builder.set_execution_dir(workspace_path)
  res_msg = ''
  try:
    builder.apply()
  except Exception,ex:
    res_msg+=ex.message+'\n'
  res =  Response(response=s_loger.result, status=200, mimetype="text/plain")
  builder.logger.close()
  return res

@app.route("/config/<identifier>/<platform>/<name>", methods=["POST"])
@crossdomain(origin="*")
def save_config(identifier, platform, name):
  print "saved"
  filepath = os.path.join(workspace_path, identifier, platform, name)
  config_loader = FileConfigLoader(filepath)
  try:
    newconf = json.loads(request.data)
    config_loader.save_config(newconf)
    print 'all fine'
    return Response(response="True", status=200)
  except Exception, ex:  # @UnusedVariable
    print ex.message
    return Response(response="False", status=200)

@app.route("/config/<identifier>/<platform>/<name>/var/<varname>", methods=["GET"])
@crossdomain(origin="*")
def get_variable(identifier, platform, name, varname):
  filepath = os.path.join(workspace_path, identifier, platform, name)
  conf = FileConfigLoader(filepath).dictionary
  res = [x for x in conf["Variables"] if x["name"] == varname][0]
  return Response(response=json.dumps(res), status=200, mimetype="application/json")

@app.route("/config/<identifier>/<platform>/<name>/<varname>", methods=["POST"])
@crossdomain(origin="*")
def save_variable(identifier, platform, name, varname):
  filepath = os.path.join(workspace_path, identifier, platform, name)
  config_loader = FileConfigLoader(filepath)
  conf = config_loader.dictionary
  res = [x for x in conf["Variables"] if x["name"] == varname][0]
  res["value"] = request.data
  config_loader.save_config(conf)
  return True

@app.route("/config/<identifier>/<platform>/<name>/res/<resid>", methods=["GET"])
@crossdomain(origin="*")
def get_resource(identifier, platform, name, resid):
  filepath = os.path.join(workspace_path, identifier, platform, name)
  conf = FileConfigLoader(filepath).dictionary
  res = [x for x in conf["Resources"] if x["rid"] == resid][0]
  file_path = os.path.join(workspace_path, identifier, platform, res['url'])
  print file_path
  if os.path.exists(file_path):
    print 'resource exists:'+file_path
    return send_file(file_path, mimetype='image/png')
  else:
    print 'non existent'
    print 'resource not available at:'+file_path
    return Response(status = 404)



@app.route("/config/<identifier>/<platform>/<name>/res/<resid>", methods=["POST"])
@crossdomain(origin="*")
def save_resource(identifier, platform, name, resid):
  filepath = os.path.join(workspace_path, identifier, platform, name)
  conf = FileConfigLoader(filepath)
  res = [x for x in conf["Resources"] if x["rid"] == resid][0]
  # data_file = request.files.get('data_file')
  files = request.files.getlist('files[]')
  file_path = os.path.join(workspace_path, identifier, platform, res['url'])
  files[0].save(file_path)
  print "File Path: %s" % file_path
  # shutil.copy(data_file, file)
  # save_file(data_file, file_name)
  # file_size = get_file_size(file_name)
  # file_url = url_for('download', file_name=file_name)
  # providing the thumbnail url is optional
  # thumbnail_url = url_for('thumbnail', file_name=file_name)
  return jsonify(name='test',
                 size=100000,
                 url='/config/%s/%s/%s' % (identifier, platform, res['url']),
                 thumbnail='/config/%s/%s/%s' % (identifier, platform, res['url']))


@app.route('/config/<path:filename>')
@crossdomain(origin="*")
def base_static(filename):
    return send_from_directory(workspace_path, filename)


@socketio.on('connect', namespace='/builds')
@crossdomain(origin="*")
def on_connect():
    emit('my response', {'data': 'Connected'})

@socketio.on('disconnect', namespace='/builds')
@crossdomain(origin="*")
def on_disconnect():
    print('Client disconnected')

def main(port):
  app.run(host="0.0.0.0", port=port, debug=True)
  socketio.run(app)

if __name__ == '__main__':
  main()  
