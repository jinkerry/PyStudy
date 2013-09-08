__author__ = 'jinfeng'

import math
import datetime

def isPrimeNumber(n):
    if (n < 2):
        return False
    max = math.sqrt(n)
    i = 2
    while(i <= max):
        if(n % i == 0):
            return False
        i += 1
    return True

def getPrimeNumberBy(n):
    i, j = 1, 1
    result = 1
    while(j < n):
        if (isPrimeNumber(i)):
            result = i
            j += 1
        i += 2
    return result

if __name__ == "__main__":
    start = datetime.datetime.now()
    print getPrimeNumberBy(10001)
    print datetime.datetime.now() - start

