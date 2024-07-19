#!/usr/bin/python3
'''0. Log parsing'''
import sys


def main():
    '''Display log stats from stdin'''
    status_codes = {
        '200': 0, '301': 0, '400': 0, '401': 0,
        '403': 0, '404': 0, '405': 0, '500': 0
    }
    lines = []
    files_size = 0
    count = 0
    try:
        for line in sys.stdin:
            lines.append(line.strip())
            count += 1
            if count == 10:
                files_size = process_lines(lines, status_codes, files_size)
                print_status(status_codes, files_size)
                count = 0
                lines = []
        files_size = process_lines(lines, status_codes, files_size)
        print_status(status_codes, files_size)
    except KeyboardInterrupt:
        files_size = process_lines(lines, status_codes, files_size)
        print_status(status_codes, files_size)
        raise


def process_lines(lines, status_codes, size):
    '''Process the lines and return total size'''
    for line in lines:
        status_code, file_size = line.split(' ')[-2:]
        if status_code in status_codes:
            status_codes[status_code] += 1
            size += int(file_size)
    return size


def print_status(status_codes, file_size):
    '''print a formated status'''
    print('File size: {:d}'.format(file_size))
    for status_code in sorted(status_codes.keys()):
        if status_codes[status_code]:
            print('{}: {:d}'.format(status_code, status_codes[status_code]))


if __name__ == '__main__':
    main()
