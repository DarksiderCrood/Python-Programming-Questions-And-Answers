'''
Given a list of tuples, extract all tuples having K digit elements.

Input : test_list = [(54, 2), (34, 55), (222, 23), (12, 45), (78, )], K = 2 
Output : [(34, 55), (12, 45), (78,)] 
Explanation : All tuples have numbers with 2 digits.

Input : test_list = [(54, 2), (34, 55), (222, 23), (12, 45), (782, )], K = 3 
Output : [(782,)] 
Explanation : All tuples have numbers with 3 digits. 
'''

test_list = [(54, 2), (34, 55), (222, 23), (12, 45), (78, )]
K = 2

test_list = [x for x in test_list if all(len(str(y))==K for y in x)] 
print(test_list)

