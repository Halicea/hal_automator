import flask
from routes import app, socketio

def main(port):
  app.run(host="0.0.0.0", port=port, debug=True)
  socketio.run(app)

if __name__ == '__main__':
  main(8080)  
