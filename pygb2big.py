# -*- coding: utf-8 -*-
import getopt
import sys


def usage():
    print('big5 file to gbk file:')
    print('\tpygb2big.py -b inputfile outputfile ')
    print('gbk file to big5 file:')
    print('\tpygb2big.py -g inputfile outputfile ')


def gb2big5(text):
    chrBIG = open('gbk2big.txt', 'rb').read()
    i = 0
    lentext = len(text)
    desc = bytearray(lentext)
    while i < lentext:
        ch1 = text[i]
        if i + 1 == lentext:
            desc[i] = ch1
            break
        ch2 = text[i + 1]
        if ch1 < 0:
            ch1 += 256
        if ch2 < 0:
            ch2 += 256

        if 0x81 <= ch1 <= 0xfe and (0x40 <= ch2 < 0x7f or 0x7f < ch2 <= 0xfe):  # is gb char
            index = ((ch1 - 0x81) * 190 + (ch2 - 0x40) - int(ch2 / 128)) * 2
            desc[i] = chrBIG[index]
            desc[i + 1] = chrBIG[index + 1]
            i += 2
        else:
            desc[i] = ch1
            i += 1
    result = desc.decode('big5', errors='ignore').strip()
    return result


def big2gb(text):
    chrGBK = open('big2gbk.txt', 'rb').read()
    i = 0
    lentext = len(text)

    desc = bytearray(lentext)
    while i < lentext:
        ch1 = text[i]
        if i + 1 == lentext:
            desc[i] = ch1
            break
        ch2 = text[i + 1]
        if ch1 < 0:
            ch1 += 256
        if ch2 < 0:
            ch2 += 256

        if 0xa1 <= ch1 <= 0xfe:  # is big5 char
            if ch2 < 0xa1:
                ch2 -= 0x40
            if ch2 >= 0xa1:
                ch2 = ch2 - 0xa1 + 0x7e - 0x40 + 1
            index = 2 * ((ch1 - 0xa1) * 157 + ch2)
            desc[i] = chrGBK[index]
            desc[i + 1] = chrGBK[index + 1]
            i += 2
        else:
            desc[i] = ch1
            i += 1
    result = desc.decode('gbk', errors='ignore').strip()
    return result


method = 'gbk2big'
try:
    options, args = getopt.getopt(sys.argv[1:], "ubg", ["usage", "big2gbk", "gbk2big"])
except getopt.GetoptError:
    sys.exit()
for name, value in options:
    if name in ("-u", "--usage"):
        usage()
        sys.exit()
    if name in ("-b", "--big2gbk"):
        method = 'big2gbk'

if not args or len(args) != 2:
    usage()
    sys.exit()

text = open(args[0], 'rb').read()
res = ''

if method == 'gbk2big':
    res = gb2big5(text)
elif method == 'big2gbk':
    res = big2gb(text)

f = open(args[1], 'w')
f.write(res)

'''s = '一系列cd魔兽世界s中文'
s2 = gb2big5(bytes(s, 'gbk'))
print(s2)
s3 = big2gb(bytes(s2, 'big5'))
print(s3)

'''
