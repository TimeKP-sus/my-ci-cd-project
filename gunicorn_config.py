# Gunicorn configuration file
import multiprocessing
import os

# Server socket
bind = "0.0.0.0:%s" % os.environ.get("PORT", 5000)
backlog = 2048

# Worker processes
workers = max(2, multiprocessing.cpu_count())
worker_class = "sync"
worker_connections = 1000
timeout = 30
keepalive = 2

# Server mechanics
daemon = False
pidfile = None
umask = 0
user = None
group = None
tmp_upload_dir = None

# Application
wsgi_app = "backend.app:app"
preload_app = False

# Logging
accesslog = "-"
access_log_format = '%(h)s %(l)s %(u)s %(t)s "%(r)s" %(s)s %(b)s "%(f)s" "%(a)s"'
errorlog = "-"
loglevel = "info"
