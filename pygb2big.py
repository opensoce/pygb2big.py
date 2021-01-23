# -*- coding: utf-8 -*-
import urllib
from urllib.parse import quote,unquote
#import wmi as wmi
#import cpuid_native
from uuid import getnode as get_mac
zone = "\\xE5\\x8A\\xA0\\xE6\\x8B\\xBF\\xE5\\xA4\\xA7"
sbutton ="%E6%8F%90%E4%BA%A4%E6%96%B0%E4%B8%BB%E9%A2%98"
html = 'abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz0123456701234567890123456789博学多才博闻强记博大精深博学多才博闻强c2s记博大精深博学多才博闻强记博大精深博学多才博闻强记博大精深博学多才博闻强记博大精深博学多才博闻强记博大精深'
def cutstr(strs, length):
    str = ''
    cnt = 0
    strs = strs.strip()
    for i in range(0, len(strs)):
        _char = strs[i]

        if '\u4e00' <= _char <= '\u9fa5':
            cnt += 3
        else:
            cnt += 1
        if cnt<length:
            str += _char
        else:
            break
    return str
'''c = wmi.WMI()
for s in c.Win32_Processor():
    print (s)'''
#print(c.ProcessorId)
#print( cutstr(html, 80))
#print(cpuid_native.get_cpuid())
mac = get_mac()
from pathlib import Path
def gb2big5(text):
    chrBIG = open('gbk2big.txt', 'rb').read(47880)
    i = 0
    lentext = len(text)
    desc = bytearray(lentext)
    while i<lentext:
        ch1 = text[i]
        if i+1 == lentext:
            desc[i] = ch1
            break
        ch2 = text[i+1]
        if ch1<0:
            ch1 += 256
        if ch2<0:
            ch2+=256

        if 0x81 <= ch1 <= 0xfe and (0x40 <= ch2 < 0x7f or 0x7f < ch2 <= 0xfe):  # is gb char
            index = ((ch1 - 0x81) * 190 + (ch2 - 0x40) - int(ch2 / 128)) * 2
            #print('index:', len(chrBIG)) print('index:', index)
            desc[i] = chrBIG[index]
            desc[i+1] = chrBIG[index+1]
            i += 2
        else:
            desc[i] = ch1
            i += 1
    result = desc.decode('big5').strip()
    return result

def big2gb(text):
    chrGBK = open('big2gbk.txt', 'rb').read()
    i = 0
    lentext = len(text)

    desc = bytearray(lentext)
    while i<lentext:
        ch1 = text[i]
        if i+1 == lentext:
            desc[i] = ch1
            break
        ch2 = text[i+1]
        if ch1<0:
            ch1 += 256
        if ch2<0:
            ch2+=256

        if 0xa1 <= ch1 <= 0xfe:  # is big5 char
            if ch2<0xa1:
                ch2 -= 0x40
            if ch2>=0xa1:
                ch2 = ch2 -0xa1 + 0x7e-0x40+1
            index = 2 * ((ch1 - 0xa1) * 157 + ch2)
            desc[i] = chrGBK[index]
            desc[i+1] = chrGBK[index+1]
            i+=2
        else:
            desc[i] = ch1
            i+=1
    result = desc.decode('gbk').strip()
    return result

s = '一系列cd魔兽世界s中文'
s2 = gb2big5(bytes(s, 'gbk'))
print(s2)
s3 = big2gb(bytes(s2, 'big5'))
print(s3)
