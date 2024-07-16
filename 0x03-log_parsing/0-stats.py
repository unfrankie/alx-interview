#!/usr/bin/python3
"""
This script reads stdin line by line and computes metrics
"""
import sys
import signal


def print_stats(total_size, status_codes):
    """
    Prints the computed metrics.
    """
    print("File size: {}".format(total_size))
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print("{}: {}".format(code, status_codes[code]))


total_size = 0
status_codes = {200: 0, 301: 0, 400: 0, 401: 0,
                403: 0, 404: 0, 405: 0, 500: 0}
line_count = 0


def signal_handler(sig, frame):
    """
    signal handling
    """
    print_stats(total_size, status_codes)
    sys.exit(0)


signal.signal(signal.SIGINT, signal_handler)
for line in sys.stdin:
    parts = line.split()
    if len(parts) < 7:
        continue
    try:
        file_size = int(parts[-1])
        total_size += file_size
        status_code = int(parts[-2])
        if status_code in status_codes:
            status_codes[status_code] += 1
    except ValueError:
        continue
    line_count += 1
    if line_count % 10 == 0:
        print_stats(total_size, status_codes)
print_stats(total_size, status_codes)
