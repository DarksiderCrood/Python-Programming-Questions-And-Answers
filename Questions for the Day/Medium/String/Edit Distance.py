
'''
Given two strings s and t. Find the minimum number of operations that need to be 
performed on str1 to convert it to str2. The possible operations are:

Insert a character at any position of the string.
Remove any character from the string.
Replace any character from the string with any other character.
 

Example 1:

Input: 
s = "geek", t = "gesek"
Output: 1
Explanation: One operation is required 
inserting 's' between two 'e's of str1.
Example 2:

Input : 
s = "gfg", t = "gfg"
Output: 
0
Explanation: Both strings are same.
'''

# Raw Solution

# s = list("geeks")
# t = list("gesek")

# if s == t:
#     print(0)
# else:
#     count = 0
#     for x,y in zip(s,t):
#         if x==y:
#             continue
#         elif y != x:
#             count+=1
#             inx = s.index(x)
#             s[inx] = y
#         elif y not in s:
#             count+=1
#             inx = s.index(x)
#             s.insert(inx+1,y)
#         elif x not in t:
#             count+=1
#             s.remove(x)
            

# s = ''.join(s)
# t = ''.join(t)
# print(s,t)
# print(count)


class Solution:
    def minmum(s, t, k, j):
        if k == 0:
            return k
        if j == 0:
            return j
        if s[k-1]== t[j-1]:
            return Solution.minmum(s, t, k-1, j-1)
        return 1 + min(Solution.minmum(s, t, k, j-1), 
                   Solution.minmum(s, t, k-1, j),
                   Solution.minmum(s, t, k-1, j-1) 
                   )
    def editDistance(self, s, t):
		# Code here
	    k = len(s)
	    j = len(t)
	    result = Solution.minmum(s,t,k,j)
		
	    return result
	


if __name__ == '__main__':
    s = 'geeks'
    t = 'gesek'
    ob = Solution()
    ans = ob.editDistance(s, t)
    print(ans)
