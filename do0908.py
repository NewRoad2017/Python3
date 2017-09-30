import sys
sys.path.append("D:/Applications/Python3/GeneralFunction")
from GeneralFunction import OperationFunction
list = [3,7,5,6,8]
listCount = len(list)
for i in range(0,listCount):
    valueCur = list[i]
    min = i
    for j in range(i+1,listCount):
        if list[min] > list[j]:
            list[min], list[j] = list[j], list[min]
print (list)