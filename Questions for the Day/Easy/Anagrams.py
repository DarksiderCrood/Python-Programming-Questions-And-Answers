'''
Count Occurences of Anagrams 
Given a word pat and a text txt. Return the count of the occurences of anagrams of the word in the text.

Example 1:

Input:
txt = forxxorfxdofr
pat = for
Output: 3
Explanation: for, orf and ofr appears
in the txt, hence answer is 3.
Example 2:

Input:
txt = aabaabaa
pat = aaba
Output: 4
Explanation: aaba is present 4 times
in txt.
'''

#User function Template for python3
class Solution:

	
	def search(self,pat, txt):
	    # code here
        n, m, ans = len(txt), len(pat), 0
        ar, br = [0]*26, [0]*26

        for i in range(m):
            ar[ord(pat[i]) - 97] += 1
            br[ord(txt[i]) - 97] += 1

        for i in range(m, n):
            if ar == br: ans += 1
            br[ord(txt[i]) - 97] += 1
            br[ord(txt[i-m]) - 97] -= 1

        return ans+1 if ar == br else ans

#{ 
#  Driver Code Starts
#Initial Template for Python 3


# Driver code 
if __name__ == "__main__": 		
    tc=int(input())
    while tc > 0:
        txt=input().strip()
        pat=input().strip()
        ob = Solution()
        ans = ob.search(pat, txt)
        print(ans)
        tc=tc-1
# } Driver Code Ends