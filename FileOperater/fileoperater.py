#encoding=utf-8
__author__ = 'jinfeng'

import os


def clean_file(root='.'):
    count = 0
    sum = 0
    dirs = os.listdir(root)
    for dir in dirs:
        name = root + '/' + dir
        if os.path.isfile(name):
            if name.find('.trash') > -1:
                size = os.stat(name).st_size
                os.remove(name)
                count += 1
                sum += size
                print 'file: ', unicode(name, 'gbk'), size
        else:
            #sub dir skip
            pass
    print 'count: ', count
    print 'sum: ', sum


if __name__ == "__main__":
    clean_file('e:/clear')

