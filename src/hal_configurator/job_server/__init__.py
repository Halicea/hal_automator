import os, sys
from celery import Celery
from hal_configurator.lib.workspace_manager import Workspace
from hal_configurator.lib.app_configurator import AppConfigurator
from hal_configurator.lib.logers import ConsoleLoger, FileLoger, StringLoger, CompositeLoger
from hal_configurator.lib import load_plugins
app = Celery('jobs', backend='redis://localhost', broker='redis://localhost')

@app.task
def execute_job(builder, workspace_path, execution_dir):
	Workspace.set(workspace_path)
	load_plugins()
	builder.set_execution_dir(execution_dir)
	builder.apply()