from flask import Flask, request, Response,send_from_directory # @UnusedImport
import os
import json
import sys
sys.path.append('../../');
from hal_configurator.lib.config_loaders import FileConfigLoader
from attributes import crossdomain

workspace_path = '/Users/mkoffice01/MyProjects/MediawireConfigurations'
app = Flask(__name__, static_folder='./static', static_url_path='')
#os.chdir(os.path.dirname(__file__))

@app.route("/config")
def list_configs():
  res =  [x for x in os.listdir(workspace_path) if os.path.isdir(os.path.join(workspace_path, x)) and not x.startswith('.')]
  return Response(response=json.dumps(res), status=200, mimetype="application/json")

@app.route("/config/<identifier>/<platform>/<name>")
@crossdomain(origin="*")
def return_json(identifier,platform, name):
  filepath = os.path.join(workspace_path, identifier,platform,name)
  config_loader = FileConfigLoader(filepath)
  conf = config_loader.load_config()
  return Response(response=json.dumps(conf), status=200, mimetype="application/json")

@app.route("/config/<identifier>/<platform>/<name>", methods=["POST"])
@crossdomain(origin="*")
def save_json(identifier,platform, name):
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


@app.route("/config/<identifier>/<platform>/<name>/<varname>", methods=["GET"])
@crossdomain(origin="*")
def get_var(identifier,platform, name, varname):
  filepath = os.path.join(workspace_path, identifier,platform,name)
  config_loader = FileConfigLoader(filepath)
  conf = config_loader.load_config()
  res= [x for x in conf["Variables"] if x["name"] == varname][0]
  return Response(response=json.dumps(res), status=200, mimetype="application/json")

@app.route("/config/<identifier>/<platform>/<name>/<varname>", methods=["POST"])
@crossdomain(origin="*")
def save_var(identifier,platform, name, res):
  filepath = os.path.join(workspace_path, identifier,platform,name)
  config_loader = FileConfigLoader(filepath)
  conf = config_loader.load_config()
  res= [x for x in conf["Variables"] if x["name"] == varname][0]
  res["value"] = request.data
  config_loader.save_config(conf)
  return True

@app.route('/config/<path:filename>')
def base_static(filename):
    return send_from_directory(workspace_path, filename)

app.run(host="0.0.0.0", port=5001,debug=True)

