#encoding=utf-8

import string

def vertical_book(str):
    print unicode('猴版', 'utf-8')
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
    print unicode('虎版', 'utf-8')
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

def duilian(str):
    print unicode('龙版', 'utf-8')
    ustrs = []
    ustr = ''
    for s in str:
        ustr = unicode(s, 'utf-8')
        ustrs.append(ustr)   

    max_length, lengths = get_max_length(ustrs)

    distance = max_length-len(ustrs[0])

    print ' ' * distance + ustrs[0]

    for i in range(0, len(ustrs[1])):
        print ustrs[1][i] + ' '*(len(ustrs[0])+6) + ustrs[2][i]



def get_max_length(str):
    lengths = []
    for s in str:
        lengths.append(len(s))
        
    max_length = max(lengths)

    return max_length, lengths


if __name__ == '__main__':
    hello = ['Hello', 'World', 'in', 'a', 'frame']
    vertical_book(hello)
    horizon_book(hello)
    chinese = ['好不威风', '拳打南山敬老院', '脚踢西湖托儿所']
    duilian(chinese)


