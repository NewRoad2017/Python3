import os
from multiprocessing import Process,Pool
import time
import random

def run_proc(name):
    print('Run child process %s (%s)...' % (name, os.getpid()))
    time.sleep(random.random() * 3)
    print('Child process %s end.' %(name))


def mainProcess():
    p = Pool(4)
    for i in range(0,10):
        print('assign child process %s' % i)
        # pro = Process(target=run_proc, args=(str(i),))
        # pro.start()
        p.apply_async(run_proc,args=(str(i),))
    p.close()
    p.join()
    print('establish the process')
    print(2)




# def run_proc(name):
#     print('Run child process %s (%s)...' % (name, os.getpid()))

# if __name__ == '__main__':
#     parentProcessid = os.getpid()
#     print ('Parent process is %s' % parentProcessid)
#     pro = Process(target=run_proc, args=('test,'))
#     print('Child process will start.')
#     pro.start()
#     pro.join()
#     print('Child process end.')
#     print(2)

# 子进程要执行的代码

#
if __name__=='__main__':
    print('Parent process %s.' % os.getpid())
    # parentProcessid = os.getpid()
    # print ('Parent process is %s' % parentProcessid)
    # pro = Process(target=run_proc, args=('test'))
    # print('Child process will start.')
    # pro.start()
    # pro.join()
    # print('Child process end.')
    mainProcess()
