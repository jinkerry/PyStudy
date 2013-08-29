__author__ = 'jinfeng'

import string

def ocr():
    f = file('ocr.txt', 'r')
    text = ''
    for line in f:
        text += line
    r = ''
    for i in text:
        if i in string.letters:
            r += i

    print r

if __name__ == '__main__':
    ocr()