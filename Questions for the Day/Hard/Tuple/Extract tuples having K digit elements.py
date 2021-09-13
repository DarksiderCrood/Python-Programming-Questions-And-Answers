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
l = []
for x in test_list:
    for j in x:
        st = str(j)
        if len(st)==K:
            l.append(int(st))

print(l)
