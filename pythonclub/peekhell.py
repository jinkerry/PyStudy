__author__ = 'jinfeng'

import pickle

def pick():
    if __name__ == "__main__":
      f = open('banner.p')
      banner = pickle.load(f)
      for i in banner:
        line = ""
        for j in i:
          line += j[0]*j[1]
        print line

if __name__ == '__main__':
    pick()