#!/usr/bin/python3
"""Reads lines from stdin and computes log metrics.

After every 10 lines, and again on a keyboard interruption, the running
total file size and the number of lines per status code are printed.
"""
import sys


def print_stats(size, status_codes):
    """Print the accumulated metrics.

    Args:
        size (int): The running total of the file sizes.
        status_codes (dict): Counts of lines keyed by status code.
    """
    print("File size: {}".format(size))
    for code in sorted(status_codes):
        print("{}: {}".format(code, status_codes[code]))


if __name__ == "__main__":
    total_size = 0
    codes = {}
    valid = ["200", "301", "400", "401", "403", "404", "405", "500"]
    counter = 0

    try:
        for line in sys.stdin:
            parts = line.split()

            try:
                total_size += int(parts[-1])
            except (IndexError, ValueError):
                pass

            try:
                if parts[-2] in valid:
                    codes[parts[-2]] = codes.get(parts[-2], 0) + 1
            except IndexError:
                pass

            counter += 1
            if counter % 10 == 0:
                print_stats(total_size, codes)

        if counter % 10 != 0:
            print_stats(total_size, codes)

    except KeyboardInterrupt:
        print_stats(total_size, codes)
        raise
