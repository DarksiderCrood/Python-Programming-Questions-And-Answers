# Exercise 1: Reverse a given list in Python
'''aLsit = [100, 200, 300, 400, 500]
print(aLsit[::-1])'''

# Exercise 2: Concatenate two lists index-wise ['My', 'name', 'is', 'Kelly']
'''list1 = ["M", "na", "i", "Ke"]
list2 = ["y", "me", "s", "lly"]
list3 = [x+y for x,y in zip(list1,list2)]
print(list3)'''

# Exercise 3: Given a Python list of numbers. Turn every item of a list into its square ['Hello Dear', 'Hello Sir', 'take Dear', 'take Sir']
'''aList = [1, 2, 3, 4, 5, 6, 7]
lst = [x**2 for x in aList]
print(lst)'''

# Exercise 4: Concatenate two lists in the following order
'''list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]
list3 = [x+y for x in list1 for y in list2]
print(list3)'''

# Exercise 5: Given a two Python list. Iterate both lists simultaneously such that list1 should display item in original order and list2 in reverse order
'''list1 = [10, 20, 30, 40]
list2 = [100, 200, 300, 400]
for x,y in zip(list1,list2[::-1]):
    print(x,y)'''

# Exercise 6: Remove empty strings from the list of strings
'''list1 = ["Mike", "", "Emma", "Kelly", "", "Brad"]
list2 = [x for x in list1 if x!='']
secondway = list(filter(None, list1))
print(list2)
print(secondway)'''

# Exercise 7: Add item 7000 after 6000 in the following Python List
'''list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
list1[2][2].append(7000)
print(list1)'''

# Exercise 8: Given a nested list extend it by adding the sub list ["h", "i", "j"] in such a way that it will look like the following list
# ['a', 'b', ['c', ['d', 'e', ['f', 'g', 'h', 'i', 'j'], 'k'], 'l'], 'm', 'n']
'''list1 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]
sub_list = ["h", "i", "j"]
lst = [list1[2][1][2].append(x) for x in sub_list]
print(list1)
list1 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]
list1[2][1][2].extend(sub_list)
print(list1)'''




