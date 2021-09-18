'''
Find the Number Occurring Odd Number of Times using Lambda expression and reduce function

Given an array of positive integers. All numbers occur even number of times 
except one number which occurs odd number of times. Find the number in O(n) time & constant space.

Examples:

Input :  [1, 2, 3, 2, 3, 1, 3]
Output :  3
'''

test_list = [1, 2, 3, 2, 3, 1, 3, 3]
occure = list(map(lambda x:str(x) if test_list.count(x)%2!=0 else "", test_list))
print(0 if len(set(''.join(occure)))==0 else set(''.join(occure)))

# Without lambda
test_list = [1, 2, 3, 2, 3, 1, 3]
even_num_occure = []
for x in test_list:
    if test_list.count(x)%2!=0:
        even_num_occure.append(x)
print(set(even_num_occure))


# Geeks for Geeks Answer
from functools import reduce

def oddTimes(input):
	print (reduce(lambda a, b: a ^ b, input))

if __name__ == "__main__":
	input = [1, 2, 3, 2, 3, 1, 3]
	oddTimes(input)
