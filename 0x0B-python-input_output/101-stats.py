#!/usr/bin/python3
"""Module contain reads stdin line by line and computes metric"""


import os

status_code = [200, 301, 400, 401, 403, 404, 405, 500]
metrics = {}
total_size = 0
line_cnt = 0
read_fd = os.pipe()
read_file = os.fdopen()
while line in read_file:
    if line_cnt == 10:
        print(f"File size: {total_size}")
        for key, value in metrics.key():
            print(f"{key}: {value}")
        metrics.clear()
        line_cnt = 0
    
    status = line.split()[2]
    if status in status_code:
        total_size += line.split()[-1]
        metrics[status] = metrics.get(status, 0) + 1
        line_cnt += 1
os.close(read_fd)
