import sys
import os
from hal_configurator.lib import load_plugins
from hal_configurator.lib import configurator_console as console
    

def main():
    load_plugins()
    if sys.argv[1] in ('-s', '--server'):
        port = 5001 
        if('-port' in sys.argv):
            port = int(sys.argv[sys.argv.index('-port')+1])
        if '-debug' in sys.argv:
            import hal_configurator.web.app as app
            app.main(port)
        else:
            import hal_configurator.web.web_server as web_server
            web_server.run_server(port)
    else:
        console.main()

if __name__ == "__main__":
    main()