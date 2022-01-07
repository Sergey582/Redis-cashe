import multiprocessing

loglevel = "info"
workers = multiprocessing.cpu_count() * 2 + 1
bind = f"0.0.0.0:80"
keepalive = 60
max_requests = 1000
max_requests_jitter = 1000
timeout = 60
