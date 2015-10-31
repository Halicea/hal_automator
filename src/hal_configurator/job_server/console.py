from __future__ import absolute_import, unicode_literals

   from __future__ import absolute_import

    from celery import Celery

    
from celery import current_app
from celery.bin import worker

def main():
	
	app = current_app._get_current_object()
    worker = worker.worker(app=app)
    options = {
        'broker': 'redis://localhost',
		'backend': 'redis://localhost',
        'loglevel': 'INFO',
        'traceback': True,
    }
    worker.run(**options)

if __name__ == '__main__':
    