"""
Anagram of String 

Given two strings S1 and S2 in lowercase, the task is to make them anagram. 
The only allowed operation is to remove a character from any string. 
Find the minimum number of characters to be deleted to make both the strings anagram. 
Two strings are called anagram of each other if one of them can be converted into another 
by rearranging its letters.

Example 1:

Input:
S1 = bcadeh
S2 = hea
Output: 3
Explanation: We need to remove b, c
and d from S1.
"""


def remAnagram(str1,str2):
    
    #add code here
    if len(str1) < len(str2):
        count = 0
        for x in str1:
            if x in str2:
                count +=1
        if count == len(str1):
            return len(str2) - count
    else:
        count = 0
        for x in str2:
            if x in str1:
                count +=1
        if count == len(str2):
            return len(str1) - count


    # Another Answer
    """
        j = 0
        t = len(str1)+len(str2)
        for i in str1 :
        j += min(str1.count(i),str2.count(i))
        str1=str1.replace(i,"")
        str2=str2.replace(i,"")
        
        return (t -2*j)
    """

#  Driver Code Starts
if __name__=='__main__':
    str1 = 'basgadhbfgvhads'
    str2 = 'sjdhgvbjdsbhvbvd'
    print(remAnagram(str1,str2))