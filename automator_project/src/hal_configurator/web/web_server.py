from flask import Flask, request, Response # @UnusedImport
import os
import json
from hal_configurator.lib.config_loaders import FileConfigLoader
from attributes import crossdomain
#setup the working directory to thisone 
#
os.chdir(os.path.dirname(__file__))
app = Flask(__name__, static_folder='static', static_url_path='')
workspace_path = '/home/costa.halicea/MediawireConfigurations'
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
    #Here you should not load the config, why would you save it?
    #you should save the dictionary you will receive from the request body..
    #read about how post works.
    config_loader.save_config(config_loader.load_config())
    return True
  except Exception, ex:  # @UnusedVariable
    return False

def run_server():
  app.run(host="0.0.0.0", port=5001,debug=True)

if __name__ == '__main__':
  run_server()
