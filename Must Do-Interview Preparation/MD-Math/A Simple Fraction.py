'''
Given a fraction. Convert it into a decimal. 
If the fractional part is repeating, enclose the repeating part in parentheses.
 

Examappingle 1:

Input: numerator = 1, denominator = 3
Output: "0.(3)"
Explanation: 1/3 = 0.3333... So here 3 is 
recurring.
Examappingle 2:

Input: numerator = 5, denominator = 2
Output: "2.5"
Explanation: 5/2 = 2.5
 

Your Task:
You don't need to read or print anyhting. Your task is to comappinglete the function fractionToDecimal() 
which takes numerator and denominator as input parameter and returns its decimal form in string format.

Note: In case, the numerator is divisible by the denominator, just print the integer value.
 

Expected Time Comappingelxity: O(k) where k is constant.
Expected Space Comappinglexity: O(k)
 

Constraints:
1 ≤ numerator, denominator ≤ 2000
'''




class Solution:
    def fractionToDecimal(self, numerator, denominator):
        if(numerator%denominator!=0):
            result = int(numerator/denominator)
            sis = ""
            sis+=str(result)
            sis+="."
            cop = numerator%denominator
            mapping = {}
            while(cop!=0 and cop not in mapping):
                mapping[cop] = len(sis)
                cop = cop * 10
                actual = cop // denominator
                sis += str(actual)
                cop = cop % denominator
                if (cop == 0):
                    return sis
                else:
                    return(sis[:mapping[cop]]+"("+sis[mapping[cop]:]+")")
        else:
            return int(numerator/denominator)


if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		numerator, denominator = input().split()
		numerator = int(numerator); denominator = int(denominator)
		ob = Solution()
		ans = ob.fractionToDecimal(numerator, denominator)
		print(ans)
