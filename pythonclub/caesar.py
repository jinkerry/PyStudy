__author__ = 'jinfeng'

def caesar():
    #hint K->M, O->Q, E-G
    original ="g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
    target = []
    for str in original:
        num = ord(str)
        if(num >= 97 and num <=120):
            target.append(chr(num + 2))
        elif(num == 121):
            target.append('a')
        elif(num == 122):
            target.append('b')
        else:
            target.append(chr(num))
    print original
    print ''.join(target)

if __name__ == '__main__':
    caesar()