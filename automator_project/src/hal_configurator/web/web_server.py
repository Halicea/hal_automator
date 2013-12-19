from flask import Flask, request
import os
import json
from hal_configurator.lib.config_loaders import FileConfigLoader

app = Flask(__name__)
workspace_path = '/home/costa.halicea/MediawireConfigurations'
@app.route("/config/<identifier>/<platform>/<name>")
def return_json(identifier,platform, name):
  filepath = os.path.join(workspace_path, identifier,platform,name)
  config_loader = FileConfigLoader(filepath)
  conf = config_loader.load_config()
  return json.dumps(conf)

@app.route("/config/<identifier>/<platform>/<name>", methods=["POST"])
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
  except Exception, ex:
    return False

def run_server():
  app.run(host="0.0.0.0", port=5001,debug=True)

if __name__ == '__main__':
  run_server()
