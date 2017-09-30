# -*- coding: utf-8 -*-
import re
import os

#替换函数
def subString(dataStr,dataPattern,dataReplace):
    newString = re.sub(dataPattern,dataReplace,dataStr)
    return newString
#路径替换函数
def replacePath(dataStr):
    strConcrete = subString(dataStr,"\\\\","/")
    return strConcrete

def MatchPattern(dataPattern,dataStr):
    pattern = re.compile(dataPattern)
    match = pattern.match(dataStr)
    return match.group()

def SearchPattern(dataPattern,dataStr):
    pattern = re.compile(dataPattern)
    result = re.search(pattern,dataStr)
    if result:
        return result.group(),result.span()
    else:
        return None

if __name__ == '__main__':
    string = 'xx'
    pattern = '[^admin/]'
    z = SearchPattern(pattern,string)
    # list = [u'（']
    # str = "（）/"
    # xx = SearchPattern('[\u4e00-\u9fa5]',str)
    # str = '<span style="font-family:\'宋体\';font-size:16px"/>'
    # str = subString(str,"\'","\'\'")
    str = '首届共享杯(大学生科技资源共享与服务创新实践竞赛/在京启动'
    str = subString(str,"[^\w\u3007\u4E00-\u9FCB\uE815-\uE864]|[/]","")
    # str = subString(str, "）", ")")
    # str = subString(str, "“", "\"")
    # str = subString(str, "”", "\"")
    xx = SearchPattern('pages/((?:[\\w\\-]+/)*)$', str)
    print("OK")

    # string = '第10次北极考察原始数据'
    # pattern = '[1-9]\d*'
    # x = SearchPattern(pattern,string)[0]
    # (string,tupIndexs) = SearchPattern(pattern,string)
    # index = tupIndexs[0]
    #pattern = '表'
    #results = SearchPattern(pattern,string)
    ## match the path
    # fileDir = r'\\192.168.30.89\share'
    # fileDir = replacePath(fileDir)
    # list = os.listdir(fileDir)
    # strPattern = '第[0-3]?[0-9]?次'
    # listResults = []
    # for item in list:
    #     if SearchPattern(strPattern,item) is not None:
    #         listResults.append(item)
    # listDir = ['第15次队原始数据', '第21次队原始数据', '第22次南极考察原始资料', '第23次队原始数据', '第24次南极考察原始资料', '第26次南极考察原始资料',
    #                    '第27次南极考察原始资料', '第6次北极考察数据管理相关文档', '第5次北极考察_数据协调', '第15次南极考察原始数据', '第21次南极考察原始数据',
    #                    '第23次南极考察原始数据', '第24次南极考察原始数据', '第26次南极考察原始数据', '第27次南极考察原始数据', '第4次北极考察原始数据', '第6次北极考察原始数据',
    #                    '第7次北极考察', '第3次北极考察原始数据', '第7次北极考察原始数据', '第8次北极考察']
    # listDir = ['第22次南极考察原始资料', '第24次南极考察原始资料', '第26次南极考察原始资料','第27次南极考察原始资料','第15次南极考察原始数据', '第21次南极考察原始数据','第23次南极考察原始数据', '第26次南极考察原始数据', '第27次南极考察原始数据']
    # dict_1 = {}
    # for item in listDir:
    #     str = SearchPattern(r'[1-9]\d*',item)[0]
    #     dict_1[item] = 'south_'+str
