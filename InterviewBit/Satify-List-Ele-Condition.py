'''
Equal
Given an array A of integers, find the index of values that satisfy A + B = C + D, 
where A,B,C & D are integers values in the array

Note:

1) Return the indices `A1 B1 C1 D1`, so that 
  A[A1] + A[B1] = A[C1] + A[D1]
  A1 < B1, C1 < D1
  A1 < C1, B1 != D1, B1 != C1 

2) If there are more than one solutions, 
   then return the tuple of values which are lexicographical smallest. 

Assume we have two solutions
S1 : A1 B1 C1 D1 ( these are values of indices int the array )  
S2 : A2 B2 C2 D2

S1 is lexicographically smaller than S2 iff
  A1 < A2 OR
  A1 = A2 AND B1 < B2 OR
  A1 = A2 AND B1 = B2 AND C1 < C2 OR 
  A1 = A2 AND B1 = B2 AND C1 = C2 AND D1 < D2
Example:

Input: [3, 4, 7, 1, 2, 9, 8]
Output: [0, 2, 3, 5] (O index)
'''

# By InterviewBit
class Solution:
    # @param A : list of integers
    # @return a list of integers
    def equal(self, A):
        n = len(A)
        if n == 0:
            return []
        sumDict = dict()
        ret = []
        '''for i in range(n):
            for j in range(i+1, n):
                temp = A[i]+A[j]
                # print temp
                if temp in sumDict:
                    existing = sumDict[temp]
                    print temp, i, j, existing
                    for k in range(0, len(existing),2):
                        if existing[k] < i:
                            ret += existing[k:k+2] + [i, j]
                            return ret
                    sumDict[temp] += [i, j]
                else:
                    sumDict[temp] = [i, j]'''
        for i in range(n):
            for j in range(i+1, n):
                temp = A[i]+A[j]
                if temp in sumDict:
                    sumDict[temp] += [i, j]
                else:
                    sumDict[temp] = [i, j]
        
        for i in range(n):
            for j in range(i+1, n):
                # print i, j
                temp = A[i]+A[j]
                if temp in sumDict:
                    tempLst = sumDict[temp]
                    # print temp, tempLst
                    if len(tempLst) >= 4:
                        ret += tempLst[0:2]
                        for k in range(2, len(tempLst), 2):
                            if tempLst[k] > ret[0] and tempLst[k] != ret[1] and tempLst[k+1] != ret[1]:
                                ret += tempLst[k:k+2]
                                return ret
                        if len(ret) < 4:
                            ret = []
        if len(ret) < 4:
            ret = []
        return ret