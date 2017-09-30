def CleantheNull(dataList):
    list = []
    dict = {}
    for index in range(0,len(dataList)):
        item = dataList[index]
        if item != "":
            dict[item] = index
            list.append(item)
    return list,dict

def Sort(dataList):
    dataList.sort()

def ListAppend(dataList,*args):
    for arg in args:
        dataList.append(arg)


if __name__ == '__main__':
    list = ["","","","fefe","","feght"]
    (listNew,dict) = CleantheNull(list)
    #Sort(list)
    print (list)
