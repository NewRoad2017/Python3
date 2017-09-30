def Join(dataPattern,*args):
    str1 = "\'"
    str2 = ' % ('
    count = len(args)
    for index in range(0,count):
        arg = args[index]

        if index == len(args) - 1:
            str1 = str1+"%s"
            str2 = str2 +  '\''+str(arg)+'\''
        else:
            str1 = str1 + "%s" + dataPattern
            str2 = str2 + '\''+str(arg)+'\'' + ','

    str1 = str1 + '\''
    str2 = str2 +')'
    strJoin = str1+str2
    return eval(strJoin)
if __name__ == '__main__':
    aa = 'a'
    str = Join(',',aa,'b','c')
    print(2)

