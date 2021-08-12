'''
Given a number, find the total number of divisors of the factorial of the number.
Since the answer can be very large, print answer modulo 10^9+7.

Input
    The first line contains T, number of testcases.
    T lines follows each containing the number N.

Output
    Print T lines of output each containing the answer.

Constraints
    1 <= T <= 500
    0 <= N <= 50000

Sample Input:
    3
    2
    3
    4

Sample Output:
    2
    4
    8
'''

t=int(input())
l=[]
for x in range(0,t):
    i=int(input())
    l.append(i)

for n in l:
    s=1
    c=0
    if n < 0:
        print("No fact for negative")
    elif n==0:
        print("fact for 0 is 1")
    else:
        for x in range(1, n+1):
            s=s*x
    #print("fact of num:",s)
    for x in range(1, s+1):
        if not s%x:
            c=c+1
            #print(x)    
    print(c)