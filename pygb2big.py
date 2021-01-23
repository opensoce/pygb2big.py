# -*- coding: utf-8 -*-
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
