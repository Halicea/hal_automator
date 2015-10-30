import os
import json
import sys
import flask
from flask import (
    Flask, request, Response, send_from_directory, jsonify,
    send_file, abort)  # @UnusedImport
import flask.ext.login as flask_login

from hal_configurator.web.routes import app, socketio, workspace_path, app_config
from hal_configurator.web.routes.auth import login_manager
from hal_configurator.web.attributes import crossdomain
from hal_configurator.job_server import execute_job
from hal_configurator.lib.config_loaders import FileConfigLoader
from hal_configurator.lib.workspace_manager import Workspace
from hal_configurator.lib.app_configurator import AppConfigurator
from hal_configurator.lib.logers import ConsoleLoger, FileLoger, StringLoger, CompositeLoger

@app.route('/')
@crossdomain(origin="*")

def root():
  return app.send_static_file('index.html')

@app.route("/config")
@flask_login.login_required
def list_configs():
  res = [x for x in os.listdir(workspace_path)
         if os.path.isdir(os.path.join(workspace_path, x)) and
         not (x.startswith('.') or x.startswith('_'))]
  return Response(response=json.dumps(res), status=200, mimetype="application/json")

@app.route("/config/jobs")
@crossdomain(origin="*")
@flask_login.login_required
def get_jobs_list():
  root = os.path.join(workspace_path, 'jobs')
  res = [x for x in os.listdir(root)
         if os.path.isfile(os.path.join(root, x)) and x.endswith('.halc') and
          not ('_vars' in x or '_ress' in x) and
          not (x.startswith('.') or x.startswith('_'))]
  return Response(response=json.dumps(res), status=200, mimetype="application/json")

@app.route("/config/<environment>")
@crossdomain(origin="*")
@flask_login.login_required
def list_environments(environment):
  root = os.path.join(workspace_path, environment)
  res = [x for x in os.listdir(root)
         if os.path.isdir(os.path.join(root, x)) and
          not (x.startswith('.') or x.startswith('_'))]
  return Response(response=json.dumps(res), status=200, mimetype="application/json")


@app.route("/config/<environment>/<name>")
@crossdomain(origin="*")
@flask_login.login_required
def list_environment_jobs(environment, name):
  root = os.path.join(workspace_path, environment, name)
  res = [x for x in os.listdir(root)
         if os.path.isfile(os.path.join(root, x)) and (x.endswith('.halc') or x == 'bc.json') and
          not (x.startswith('.') or x.startswith('_'))]
  
  return Response(response=json.dumps(res), status=200, mimetype="application/json")


@app.route("/config/<identifier>/<platform>/<name>")
@crossdomain(origin="*")
@flask_login.login_required
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
@flask_login.login_required
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
@flask_login.login_required
def run_config(identifier, platform, name):
  Workspace.set(workspace_path)
  filepath = os.path.join(workspace_path, identifier, platform, name)
  loader = FileConfigLoader(filepath)
  config = loader.dictionary
  c_loger = ConsoleLoger()
  s_loger = StringLoger()
  composite_log = CompositeLoger(*[c_loger, s_loger])
  builder = AppConfigurator(loader, composite_log)
  working_dir = request.args.get('wd')
  if working_dir:
    builder.set_execution_dir(working_dir)
  else:
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
@flask_login.login_required
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
@flask_login.login_required
def get_variable(identifier, platform, name, varname):
  filepath = os.path.join(workspace_path, identifier, platform, name)
  conf = FileConfigLoader(filepath).dictionary
  res = [x for x in conf["Variables"] if x["name"] == varname][0]
  return Response(response=json.dumps(res), status=200, mimetype="application/json")

@app.route("/config/<identifier>/<platform>/<name>/<varname>", methods=["POST"])
@crossdomain(origin="*")
@flask_login.login_required
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
@flask_login.login_required
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
@flask_login.login_required
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




