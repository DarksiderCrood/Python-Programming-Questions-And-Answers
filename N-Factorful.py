'''
A number is called n-factorful if it has exactly n distinct prime factors. 
Given positive integers a, b, and n, your task is to find the number of integers between a and b, 
inclusive, that are n-factorful. We consider 1 to be 0-factorful.

Input
Your input will consist of a single integer T followed by a newline and T test cases. 
Each test cases consists of a single line containing integers a, b, and n as described above.

Output
Output for each test case one line containing the number of n-factorful integers in [a, b].

Constraints
T < 10000

1 ≤ a ≤ b ≤ 10^6

0 ≤ n ≤ 10

Sample Input
5
1 3 1
1 10 2
1 10 3
1 100 3
1 1000 0

Sample Output
2 
2
0
8
1
'''

import math


prime_nums = []


def distinct_factors():
	n = 10000
	new_val = int((n - 2) / 2)
	checked_val = [False] * (new_val + 1)
	for i in range(1, new_val + 1):
		j = i
		while ((i + j + 2 * i * j) <= new_val):
			checked_val[i + j + 2 * i * j] = True
			j += 1
	prime_nums.append(2)
	for i in range(1, new_val + 1):
		if (checked_val[i] == False):
			prime_nums.append(2 * i + 1)


def N_Factorful(a, b, n):
	distinct_factors()
	result = 0
	for i in range(a, b + 1):
		tmp = math.sqrt(i)
		copy = i
		count = 0
		j = 0
		while (prime_nums[j] <= tmp):
			if (copy % prime_nums[j] == 0):
				count += 1
				while (copy % prime_nums[j] == 0):
					copy = (copy // prime_nums[j])
			j += 1
		if (copy != 1):
			count += 1
		if (count == n):
			result += 1
	return result


if __name__ == '__main__':
    a = 1
    b = 100
    n = 3
    print(N_Factorful(a, b, n))


# or

n = 1000000
prime= [1]*(n+1)
ans = [0]*(n+1)
def compute():
    prime[0]=0;
    prime[1]=0;
    i = 2
    while(i*i<=n):
        if(prime[i]==1):
            j = i*i
            while(j<=n):
                prime[j]=0
                j=j+i
        i+=1
    i=2
    while(i<=n):
        if(prime[i]==1):
            ans[i]+=1
            j = i*2
            while(j<=n):
                ans[j]+=1
                j=j+i
        i+=1

#main
t = int(input())
compute()
for _ in range(0,t):
    inp = list(map(int,input().split()))
    a = inp[0]
    b = inp[1]
    n = inp[2]
    count=0
    i=a
    while(i<=b):
        if(ans[i]==n):
            count+=1
        i+=1
    print(count)