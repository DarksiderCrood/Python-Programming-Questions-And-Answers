'''
Find the Number Occurring Odd Number of Times using Lambda expression and reduce function

Given an array of positive integers. All numbers occur even number of times 
except one number which occurs odd number of times. Find the number in O(n) time & constant space.

Examples:

Input :  [1, 2, 3, 2, 3, 1, 3]
Output :  3
'''

test_list = [1, 2, 3, 2, 3, 1, 3]

occure = list(map(lambda x:test_list.count(x)!=0, test_list))
print(occure)

for x in test_list:
    print(test_list.count(x))