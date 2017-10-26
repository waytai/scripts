#########################################################################
# -*- coding:utf-8 -*-
# File Name: liu.py
#########################################################################
# !/binn(string_num):

import ConfigParser
import os


def get_config(section, key):
    config = ConfigParser.ConfigParser()
    base_path = os.path.split(os.path.realpath(__file__))
    site_type = 'main'
    path = base_path[0] + '/config/consumer_%s.conf' % site_type
    print path
    config.read(path)
    return config.get(section, key)


base = [str(x) for x in range(10)] + [chr(x) for x in range(ord('A'), ord('A') + 6)]


def dec2bin(string_num):
    num = int(string_num)
    mid = []
    while True:
        if num == 0: break
        num, rem = divmod(num, 2)
        mid.append(base[rem])

    return ''.join([str(x) for x in mid[::-1]])


def hex2dec(string_num):
    return str(int(string_num.upper(), 16))


def hex2bin(string_num):
    return dec2bin(hex2dec(string_num.upper()))


def bin2dec(string_num):
    return str(int(string_num, 2))


def dec2hex(string_num):
    num = int(string_num)
    mid = []
    while True:
        if num == 0: break
        num, rem = divmod(num, 16)
        mid.append(base[rem])
    return ''.join([str(x) for x in mid[::-1]])


def bin2hex(string_num):
    return dec2hex(bin2dec(string_num))


def al_check(test_data):
    el_sum = 0
    for i in xrange(len(test_data) / 2):
        start = 2 * i
        end = 2 * i + 2
        element = test_data[start:end]
        el_sum += int(element[0], 16) * 16 + int(element[1], 16)
    el_sum = ~el_sum + 1
    mod = el_sum % 256
    cs = hex(mod).replace('0x', '')
    if len(cs) == 1:
        cs = '0' + cs
    return cs.upper()


#if __name__ == "__main__":
#    a = hex2bin("28")
#    print a
