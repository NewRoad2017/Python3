import os
import abc
import sys, errno
import stat as st
import time

def PrintCostTime(dataFunction):
    def wrapper(*args,**kwargs):
        timeB = time.clock()
        count = dataFunction(*args,**kwargs)
        timeE = time.clock()
        print (str(timeE - timeB))
        return count
    return wrapper

@PrintCostTime
def getCount1(dataDirPath):
    count = 0
    for a,b,c in os.walk(dataDirPath):
        count = count +1
    return count

@PrintCostTime
def getCount2(dataDirPath):
    return len(os.listdir(dataDirPath))



if __name__ == '__main__':
    dirPath = r'C:\Users\chenlu\Desktop\word Version\words\south_33'
    count = getCount1(dirPath)

    # x = range(2)
    # list = list(x)

    print("OK")