import time

# 2 nest
import functools


# def log(dataFunc):
#     @functools.wraps(dataFunc)
#     def wrapper(*args,**kwargs):
#         print('begin call %s' % dataFunc.__name__)
#         result = dataFunc()
#         print('%s call end' % dataFunc.__name__)
#         return result
#     return wrapper


def log(*args,**kwargs):
    def decorator(dataFunc):
        @functools.wraps(dataFunc)
        def wrapper(*args, **kwargs):
            print('%s %s' % (text,dataFunc.__name__))
            result = dataFunc()
            print('%s call end' % dataFunc.__name__)
            return result
        return wrapper
    return decorator

@log
def GetNow():
    timeCur = time.localtime(time.time())
    timeStr = time.strftime("%Y-%m-%d %H:%M",timeCur)
    return timeStr



if __name__ == '__main__':
    # GetNow = log2('execute')(GetNow)
    # GetNow = log(GetNow)# let the content not to execute
    result = GetNow()
    # GetNow(GetNow)

    # func = GetNow
    # func("OK")
    # funcName = func.__name__
    print("OK")
