import threading,time
def GetNow(data):
    timeCur = time.localtime(time.time())
    timeStr = time.strftime(timeCur)
    print (timeStr)
if __name__ == '__main__':
    x = threading.current_thread()
    print("thread %s is running" % threading.current_thread().name)
    thread = threading.Thread(GetNow,name="localThread",args=("OK",))
    thread.start()

