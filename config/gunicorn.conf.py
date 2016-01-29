import multiprocessing

bind = "unix:/tmp/kool967.sock"
workers = multiprocessing.cpu_count() * 2 + 1
