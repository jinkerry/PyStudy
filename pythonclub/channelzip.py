__author__ = 'jinfeng'

import zipfile
import re

def unzip():
    path = 'channel'
    zipFile = zipfile.ZipFile( 'channel.zip')
    print zipFile.namelist()
    zipFile.extractall(path)
    answer = '90052'
    while(1):
        f = open(path + '/' + answer + '.txt')
        text = f.readline()
        print text
        patt = '\d+$'
        r = re.findall(patt, text)
        if(len(r) == 0):
            break;
        answer = r[0]

if __name__ == '__main__':
    unzip()