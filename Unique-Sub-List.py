'''
Given a string, reduce it in Such a way that all Of its
substrings are distinct. To do so, you may delete
any characters at any index, What is the minimum
number of deletions needed?
'''

from collections import Counter

def test_dist(lsts):
    lists = []
    for i in range(len(lsts) + 1):
        for j in range(i):
            lists.append(lsts[j: i])
    dis = set(lists)
    return dis

def test_sub(l):
    lists = []
    for i in range(len(l) + 1):
        for j in range(i):
            lists.append(l[j: i])

    lh = len(set(lists))
    Dict = dict(Counter(lists))
    add = 0    
    for value in Dict.values():
        add += value
    if lh == add:
        return True    
    else:
        return False


lst = 'abab'
result = test_dist(lst)
count = 0
all_pass = []
for x in result:
    count += 1    
    res = lst.replace(x, '', 1)
    result = test_sub(res)
    if result:
        all_pass.append(len(x))
print("Minimum deletion required: ", min(all_pass))