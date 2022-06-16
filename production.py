import os

os.system(
    'gunicorn '
    'main:gunicorn_binder '
    '--bind 0.0.0.0:5000 '
    '--worker-class aiohttp.GunicornWebWorker '
    '--workers 12'
)