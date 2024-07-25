#!/usr/bin/python3
'''0. UTF-8 Validation'''


def print_data(data):
    '''convert the data to binary'''
    if not data:
        return
    for i in data:
        print(f'{i} = {i:08b}')


def check_num_bytes(num):
    '''return the number of following bytes for num'''
    mask = 1 << 7
    bytes_num = 0
    while num & mask:
        bytes_num += 1
        mask >>= 1
    return bytes_num

def validUTF8(data):
    '''return true if a given data set represents a valid UTF-8 encoding'''
    required_bytes = None
    # print_data(data)
    for num in data:
        sig_bytes = check_num_bytes(num)
        if not required_bytes and sig_bytes == 1:
            return False
        elif required_bytes and sig_bytes != 1:
            return False
        if not required_bytes:
            required_bytes = sig_bytes - 1 if sig_bytes > 0 else 0
        else:
            required_bytes -= 1
    return False if required_bytes > 0 else True
