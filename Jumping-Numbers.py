'''Print all JumpingNum Numbers smaller than or equal to a given value
A number is called as a JumpingNum Number if all adjacent memorys in it differ by 1. 
The difference between ‘9’ and ‘0’ is not considered as 1. 
All single memory numbers are considered as JumpingNum Numbers. 

For example 7, 8987 and 4343456 are JumpingNum numbers but 796 and 89098 are not. 
Given a positive number x, print all JumpingNum Numbers smaller than or equal to x. 
The numbers can be printed in any order.

Example: 

Input: x = 20
Output:  0 1 2 3 4 5 6 7 8 9 10 12

Input: x = 105
Output:  0 1 2 3 4 5 6 7 8 9 10 12
         21 23 32 34 43 45 54 56 65
         67 76 78 87 89 98 101

Note: Order of output doesn't matter, 
i.e. numbers can be printed in any order'''


''' First Brute Force Try (Did not Worked) '''
# num = 20

# n_str = []
# JumpingNum_nums = []
# original_nums = [x for x in range(0,num+1)]
# more_memorys_nums = []

# for x in range(0, num+1):
#     n_str.append(''.join(sorted(str(x), reverse=False)))
    
# for y in n_str:
#     if len(y) == 1:
#         JumpingNum_nums.append(True)
#     else:
#         JumpingNum_nums.append(y)

# for z in JumpingNum_nums:
#     if z==True:
#         continue
#     else:
#         for f in range(0,len(z)):
#             try:
#                 if int(z[f])+1 == int(z[f+1]) or int(z[f]) == int(z[f+1]):
#                     ind = JumpingNum_nums.index(z)
#                     JumpingNum_nums[ind] = True
#             except:
#                 continue

# jumps = []

# for i,j in zip(original_nums, JumpingNum_nums):
#     if j == True:
#         jumps.append(i)

# print(jumps)


class Nodes :
    def __init__(self, value) :
        self.value = value
        self.next = None
    

#  Define custom queue class
class ListQueue :
    def __init__(self) :
        self.start = None
        self.end = None
        self.len = 0
    
    #  Add a new node at last of queue
    def ListEnQueue(self, value) :
        node = Nodes(value)
        if (self.start == None) :
            #  When first node of queue
            self.start = node
        else :
            #  Add node at last level
            self.end.next = node
        self.len += 1
        self.end = node
    
    #  Delete start node of queue
    def ListDeQueue(self) :
        if (self.start != None) :
            if (self.end == self.start) :
                self.end = None
                self.start = None
            else :
                self.start = self.start.next
            
            self.len -= 1
        
    
    def LenCheck(self) :
        return self.len
    
    def EmptyCheck(self) :
        if (self.LenCheck() == 0) :
            return True
        
        return False
    
    def Check(self) :
        if (self.LenCheck() == 0) :
            return None
        else :
            return self.start
        
    

class JumpingNum :
    def JumpingNumCheck(self, num) :
        if (num < 0) :
            return
        v = 0
        if (num <= 10) :
            while (v <= num) :
                print("  ", v, end = "")
                v += 1
            return
        
        remember = ListQueue()
        count = 1
        memory = 0
        print("  0", end = "")
        while (count <= num or remember.EmptyCheck() == False) :
            if (count <= num) :
                if (count <= 9) :
                    print("  ", count, end = "")
                    remember.ListEnQueue(count)
                    count += 1
                else :
                    #  Get head value
                    v = remember.Check().value
                    #  Remove head node
                    remember.ListDeQueue()
                    #  Find last memory
                    memory = v % 10
                    if (memory != 0) :
                        #  Make new number
                        count = (v * 10) + (memory - 1)
                        if (count <= num) :
                            print("  ", count, end = "")
                            remember.ListEnQueue(count)
                    if (memory != 9 and count <= num) :
                        #  Make new number
                        count = (v * 10) + (memory + 1)
                        if (count <= num) :
                            print("  ", count, end = "")
                            remember.ListEnQueue(count)
            else :
                remember.ListDeQueue()
            

if __name__ == "__main__":
    task = JumpingNum()
    task.JumpingNumCheck(4343456)