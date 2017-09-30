import os
import sys
sys.path.append('D:/Applications/Python3/GeneralFunction')
from GeneralFunction import *
from shutil import copy
import threading,queue
from queue import Queue
import time,random


class Worker(threading.Thread):
    def __init__(self,dataQueue):
        super(Worker,self).__init__()
        self.q = dataQueue
    def run(self):
        while True:#listen if there has a task,when a task is OK
            print('RUNNING %s' % (self.name))
            listArgs = self.q.get(block = True)#try
            print('%s: get the filePath : %s' % (self.name,listArgs[0]))
            Extractfiles(listArgs[0],listArgs[1],listArgs[2],listArgs[3],listArgs[4])
            #time.sleep(random.random() * int(task))
            # print('%s :END the path %s' % (self.name,listArgs[0]))
            self.q.task_done()
            if self.q.qsize() == 0:
                break
            # if not self.q.join():
            #     break
        print('END %s' % self.name)

def BuildPool(dataQueue,dataSize):
    listWorkers = []
    for index in range(dataSize):
        worker = Worker(dataQueue)
        worker.start()
        listWorkers.append(worker)
    return listWorkers


class MyThread(threading.Thread):
    def __init__(self,arg):
        super(MyThread,self).__init__()
        self.arg = arg
    def run(self):
        print('RUNNING %s,arg %s' % (self.name,self.arg))
        # time.sleep(random.random() * 3)
        Extractfiles()
        print('END %s' % (self.name,self.arg))


# def test():
#     print('Run child process %s (%s)...' % (name, os.getpid()))
#     time.sleep(random.random() * 3)
#     print('Child process %s end.' %(name))

def Extractfiles(dataOriDir, dataTarDir, dataExtensions,dataLog,dataQueue):
    dataLog.PrepareWrite("RUNING %s,the path is %s" % (threading.current_thread().name,dataOriDir))
    listFiles = FileHelper.GetDirfiles(dataOriDir)
    for fileName in listFiles:
        filePath = PathHelper.CombinePathpurely(dataOriDir, fileName)
        if os.path.isfile(filePath):
            listFileParts = os.path.splitext(fileName)
            for extension in dataExtensions:
                if listFileParts[1] == extension:
                    print('    %s,file: %s' % (threading.current_thread().name, fileName))
                    tarFilePath = PathHelper.CombinefilePath(dataTarDir,threading.current_thread().name + "_"+fileName,extension)
                    FileHelper.DulplicateFile(filePath, tarFilePath)
                    break
        else:
            dataLog.PrepareWrite("%s ADD QUEUE:for %s" % (threading.current_thread().name,filePath))
            dataQueue.put([filePath,dataTarDir,dataExtensions,dataLog,dataQueue])
    # print(threading.current_thread().is_alive())
    dataLog.PrepareWrite("END %s ,the path is %s" % (threading.current_thread().name,dataOriDir))

if __name__ == '__main__':
    log = Logging.CreateLog()
    parentProcessid = os.getpid()
    log.PrepareWrite('Parent process is %s' % parentProcessid)
    timeB = time.clock()
    pathDir = r'\\192.168.30.89\share\第29次南极考察原始数据（不包括田启国提交的天文数据）'
    # # pathDir = r'C:\Users\chenlu\Desktop\tests\test0920\test1'
    pathDir = ReHelper.replacePath(pathDir)
    tarDir = r'C:\Users\chenlu\Desktop\word Version\words\south_29'
    tarDir = ReHelper.replacePath(tarDir)
    # listFolders = []
    # listFolders = ExtractFolders(pathDir, listFolders)
    print('----waiting for finish------')
    myqueue = Queue()
    myqueue.put([pathDir,tarDir,['.docx','.doc'],log,myqueue])
    listWorkers = BuildPool(myqueue,500)
    myqueue.join()
    # for worker in listWorkers:
    #     worker.join()
    print("queue is OK")
    timeE = time.clock()
    print('cost time is %s' % str(timeE-timeB))

