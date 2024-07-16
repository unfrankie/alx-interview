#!/usr/bin/python3
import sys


def print_stats(total_size, status_codes):
    print(f"File size: {total_size}")
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print(f"{code}: {status_codes[code]}")


def main():
    total_size = 0
    status_codes = {code: 0 for code in [200, 301, 400, 401,
                                         403, 404, 405, 500]}
    line_count = 0

    try:
        for line in sys.stdin:
            parts = line.split()
            if len(parts) != 9 or not parts[8].isdigit():
                continue

            status_code = int(parts[7])
            file_size = int(parts[8])

            if status_code in status_codes:
                status_codes[status_code] += 1
            total_size += file_size
            line_count += 1

            if line_count % 10 == 0:
                print_stats(total_size, status_codes)

    except KeyboardInterrupt:
        print_stats(total_size, status_codes)
        raise


if __name__ == "__main__":
    main()
