'''
You are given a string s of lower case english alphabets. You can choose any two characters 
in the string and replace all the occurences of the first character with the second character 
and replace all the occurences of the second character with the first character. 
Your aim is to find the lexicographically smallest string that can be obtained 
by doing this operation at most once.

Example 1:

Input:
A = "ccad"
Output: "aacd"
Explanation:
In ccad, we choose ‘a’ and ‘c’ and after 
doing the replacement operation once we get, 
aacd and this is the lexicographically
smallest string possible. 
 

Example 2:

Input:
A = "abba"
Output: "abba"
Explanation:
In abba, we can get baab after doing the 
replacement operation once for ‘a’ and ‘b’ 
but that is not lexicographically smaller 
than abba. So, the answer is abba. 

Your Task:  
You don't need to read input or print anything. Your task is to complete the function 
chooseandswap() which takes the string A as input parameters and returns the 
lexicographically smallest string that is possible after doing the operation at most once.

Expected Time Complexity: O(|A|) length of the string A
Expected Auxiliary Space: O(1)

 

Constraints:
1<= |A| <=105
'''


class Solution:
    def chooseandswap (self, A):
        VAL = 256
        A_list = [g for g in A]
        le = len(A_list)
        i = 0
        j = 0
        range_vals=[0 for i in range(VAL)]
        for i in range(VAL):
            range_vals[i] = -1
        for i in range(le):
            if (range_vals[ord(A_list[i])-97] == -1):
                range_vals[ord(A_list[i])-97] = i
        for  i in range(le):
            status = False
            for j in range(ord(A_list[i])-97):
                if (range_vals[j] > range_vals[ord(A[i])-97]):
                    status = True
                    break
            if (status):
                break
        if (i < le):
            char1 = (A_list[i])
            char2 = chr(j+97)
            for i in range(le):
                if (A_list[i] == char1):
                    A_list[i] = char2
                elif (A_list[i] == char2):
                    A_list[i] = char1
        return "".join(A_list)


if __name__ == '__main__': 
    ob = Solution()
    t = int (input ())
    for _ in range (t):
        A = input()
        ans = ob.chooseandswap(A)
        print(ans)



# or


def smallestStr(str, n):
	i, j=0,0

	chk=[-1]*26

	for i in range(n):
		if (chk[ord(str[i])-97] == -1):
			chk[ord(str[i])-97] = i

	for i in range(n):
		flag = False
		for j in range(ord(str[i])-97):
			if (chk[j] > chk[ord(str[i])-97]):
				flag = True
				break
		if (flag):
			break
	if (i < n):
		ch1 = (str[i])
		ch2 = chr(j+97)
		for i in range(n):
			if (str[i] == ch1):
				str[i] = ch2

			elif (str[i] == ch2):
				str[i] = ch1

	return "".join(str)

st = "z" #input()
str=list(st)
n = len(str)

print(smallestStr(str, n))