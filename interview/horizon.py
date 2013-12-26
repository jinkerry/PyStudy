#encoding=utf-8

import string

def vertical_book(str):

    max_length, lengths = get_max_length(str)

    print '*' * (max_length + 4)

    i = 0
    loop = len(str)
    while i < loop:
        s = str[i]
        l = lengths[i]
        if l < max_length:
            for j in range(0, max_length-l):
                s += ' '
        print '* %s *' % s
        i += 1

    print '*' * (max_length + 4)


def horizon_book(str):
    """

    :param str:
    """
    str.reverse()
    max_length, lengths = get_max_length(str)

    print '*' * (max_length + 4)

    temp = ''
    temps = []

    for i in range(0, max_length):
        for s in str:
            if len(s) > i:
                temp = temp + s[i]
            else:
                temp += ' '
        temps.append('* ' + temp + ' *')
        temp = ''

    for t in temps:
        print t

    print '*' * (max_length + 4)


def get_max_length(str):
    print str
    lengths = []
    for s in str:
        lengths.append(len(s))
        
    max_length = max(lengths)

    return max_length, lengths


if __name__ == '__main__':
    hello = ['Hello', 'World', 'in', 'a', 'frame']
    vertical_book(hello)
    horizon_book(hello)

