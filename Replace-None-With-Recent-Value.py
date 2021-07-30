'''
Given an array containing None values fill in the None values with most recent non None 
value in the array.
Test case:
    array = [1,None,2,3,None,None,5,None]
    output = [1, 1, 2, 3, 3, 3, 5, 5]
'''

class Replace_None:
    def __init__(self, li):
        self.lst = li
    def replace(self):
        mem = self.lst
        for x in range(0, len(mem)):
            if x == 0 and mem[x] == None:
                mem[x] = 0
            if mem[x] == None and x > 0:
                mem[x] = mem[x-1]
        return mem


if __name__ == '__main__':
    l = [None,1,None,2,3,None,None,5,None]
    rep = Replace_None(l)
    result = rep.replace()
    print(result)