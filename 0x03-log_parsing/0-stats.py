#!/usr/bin/python3
import sys

# Initialize variables
total_size = 0
status_codes = {
    "200": 0,
    "301": 0,
    "400": 0,
    "401": 0,
    "403": 0,
    "404": 0,
    "405": 0,
    "500": 0
}
line_count = 0

def print_stats():
    """ Print the statistics of the logs """
    print(f"File size: {total_size}")
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print(f"{code}: {status_codes[code]}")

try:
    for line in sys.stdin:
        # Split the line into components
        parts = line.split()

        # Ensure the line has at least 7 parts for IP, date, request, status, and file size
        if len(parts) < 7:
            continue

        # Extract the file size
        try:
            size = int(parts[-1])
            total_size += size
        except ValueError:
            continue

        # Extract the status code
        status_code = parts[-2]

        # Update the status code count if it's a valid one
        if status_code in status_codes:
            status_codes[status_code] += 1

        # Increment the line count and print stats every 10 lines
        line_count += 1
        if line_count % 10 == 0:
            print_stats()

except KeyboardInterrupt:
    # On keyboard interrupt (Ctrl + C), print the final stats
    print_stats()
    raise

# Ensure to print stats after all lines are processed
print_stats()
