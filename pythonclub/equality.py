#encoding=utf-8
__author__ = 'jinfeng'

import re

def equality():
    f = file('equality.txt', 'r')
    text = ''
    for line in f:
        text += line
    #找出两边都是三个连续大写字母的小写字母
    #One small letter, surrounded by EXACTLY three big bodyguards on each of its sides
    pattern = '[a-z][A-Z]{3}([a-z])[A-Z]{3}[a-z]'
    all = re.findall(pattern, text)
    print ''.join(all)

if __name__ == '__main__':
    equality()