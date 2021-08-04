'''
Amicable Numbers
Problem 21
Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.
For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.
Evaluate the sum of all the amicable numbers under 10000.
'''

from __future__ import print_function
from math import sqrt



def divisors_sum(n):
	tl = 0
	for i in range(1, int(sqrt(n)+1)):
		if n%i == 0 and i != sqrt(n):
			tl += i + n//i
		elif i == sqrt(n):
			tl += i
	return tl-n


if __name__ == '__main__':
	totals = []
	tl = 0

	for i in range(1, 10000):
		n = divisors_sum(i)
		
		if n < len(totals):
			if totals[n-1] == i:
				tl += n + i
		totals.append(n)

	print(tl)