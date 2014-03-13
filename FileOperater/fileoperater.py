#encoding=utf-8
__author__ = 'jinfeng'

import os


def clean_file(user_dir='.'):
    count = 0
    sum = 0
    for root, dirs, files in os.walk(user_dir):
        for file in files:
            if file.endswith('.trash'):
                full_filename = os.path.join(root, file)
                size = os.path.getsize(full_filename)
                os.remove(full_filename)
                count += 1
                sum += size
            else:
                pass
    print 'count: ', count
    print 'sum: ', sum


if __name__ == "__main__":
    clean_file('e:/clear')

