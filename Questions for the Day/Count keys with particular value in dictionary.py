inp = {'A' : 2,'B':2,'C':1, 'D':1,'E':2}

valueList = inp.values()
newDict = dict.fromkeys(valueList,0)

for key in inp.keys():
    newDict[inp[key]]+=1

print(newDict)