from flask import Flask, request, Response,send_from_directory, url_for, jsonify, send_file,abort # @UnusedImport
import os
import json
import sys
current_dir = os.path.dirname(__file__)
sys.path.append(os.path.join('../../', current_dir))
from hal_configurator.lib.config_loaders import FileConfigLoader
from attributes import crossdomain

app_config = json.loads(open(os.path.join(current_dir,'config.json'), 'r').read())
workspace_path = app_config['workspace_path']
app = Flask(__name__, static_folder='./static', static_url_path='')
#os.chdir(os.path.dirname(__file__))

@app.route("/config")
def list_configs():
  res =  [x for x in os.listdir(workspace_path) if os.path.isdir(os.path.join(workspace_path, x)) and not x.startswith('.')]
  return Response(response=json.dumps(res), status=200, mimetype="application/json")

@app.route("/config/<identifier>/<platform>/<name>")
@crossdomain(origin="*")
def get_config(identifier,platform, name):
  filepath = os.path.join(workspace_path, identifier,platform,name)
  config_loader = FileConfigLoader(filepath)
  conf = config_loader.load_config()
  return Response(response=json.dumps(conf), status=200, mimetype="application/json")

@app.route("/config/<identifier>/<platform>/<name>", methods=["POST"])
@crossdomain(origin="*")
def save_config(identifier,platform, name):
  print "saved"
  filepath = os.path.join(workspace_path, identifier,platform,name)
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
def get_variable(identifier,platform, name, varname):
  filepath = os.path.join(workspace_path, identifier,platform,name)
  config_loader = FileConfigLoader(filepath)
  conf = config_loader.load_config()
  res= [x for x in conf["Variables"] if x["name"] == varname][0]
  return Response(response=json.dumps(res), status=200, mimetype="application/json")

@app.route("/config/<identifier>/<platform>/<name>/<varname>", methods=["POST"])
@crossdomain(origin="*")
def save_variable(identifier,platform, name, res):
  filepath = os.path.join(workspace_path, identifier,platform,name)
  config_loader = FileConfigLoader(filepath)
  conf = config_loader.load_config()
  res= [x for x in conf["Variables"] if x["name"] == varname][0]
  res["value"] = request.data
  config_loader.save_config(conf)
  return True

@app.route("/config/<identifier>/<platform>/<name>/res/<resid>", methods=["GET"])
@crossdomain(origin="*")
def get_resource(identifier,platform, name, resid):
  filepath = os.path.join(workspace_path, identifier,platform,name)
  config_loader = FileConfigLoader(filepath)
  conf = config_loader.load_config()
  res=[x for x in conf["Resources"] if x["rid"] == resid][0]
  file_path = os.path.join(workspace_path, identifier, platform, res['url'])
  print file_path
  if os.path.exists(file_path):
    print 'exists'
    return send_file(file_path, mimetype='image/png')
  else:
    print 'non existent'
    return abort(404)


@app.route("/config/<identifier>/<platform>/<name>/res/<resid>", methods=["POST"])
@crossdomain(origin="*")
def save_resource(identifier, platform, name, resid):
  filepath = os.path.join(workspace_path, identifier,platform,name)
  config_loader = FileConfigLoader(filepath)
  conf = config_loader.load_config()
  res=[x for x in conf["Resources"] if x["rid"] == resid][0]
  data_file = request.files.get('data_file')
  #filename = data_file.filename
  print dir(data_file)
  print data_file
  print request.files[0]
  file_path = os.path.join(workspace_path, identifier, platform, res['url'])
  #shutil.copy(data_file, file)
  print file_path
  #save_file(data_file, file_name)
  #file_size = get_file_size(file_name)
  #file_url = url_for('download', file_name=file_name)
  # providing the thumbnail url is optional
  #thumbnail_url = url_for('thumbnail', file_name=file_name)
  return jsonify(name='test',
                 size=100000,
                 url='/config/%s/%s/%s'%(identifier, platform, res['url']),
                 thumbnail='/config/%s/%s/%s'%(identifier, platform, res['url']))


@app.route('/config/<path:filename>')
def base_static(filename):
    return send_from_directory(workspace_path, filename)

app.run(host="0.0.0.0", port=5001,debug=True)

