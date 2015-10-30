#!/Users/halicea/envs/hal_automator/bin/python
import sys
import os
from hal_configurator.lib import load_plugins
from hal_configurator.lib import configurator_console as console
try:
    from PySide import QtGui
except:
    pass
    

def main():
    load_plugins()
    if len(sys.argv) == 1 or sys.argv[1] == '-admin':
        if try_gui_imports():
            admin_mode = len(sys.argv) > 1 and sys.argv[1] == '-admin'
            main_gui(admin_mode)
        else:
            print 'Cannot open the gui mode, please see the Warning above'
    elif sys.argv[1] == '-web':
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


def try_gui_imports():
    ui_enabled = True
    try:
        from PySide import QtGui
    except Exception, ex:
        ui_enabled = False
        print ex
        print "Warning: PySide is not installed, Gui Mode is not possible, please execute: 'pip install -U PySide' to enable the gui mode"
    return ui_enabled


def main_gui(isAdmin):
    from hal_configurator.ui.configwindow import ConfigWindow
    app = QtGui.QApplication(sys.argv)
    mw = ConfigWindow(None)
    mw.show()
    app.setWindowIcon(QtGui.QIcon())
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()