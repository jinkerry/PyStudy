__author__ = 'jinfeng'

import string

def caesar():
    #hint K->M, O->Q, E-G
    original ="g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. " \
              "bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. " \
              "sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
    t = string.maketrans('abcdefghijklmnopqrstuvwzyz', 'cdefghijklmnopqrstuvwzyzab')
    print original.translate(t)

if __name__ == '__main__':
    caesar()
