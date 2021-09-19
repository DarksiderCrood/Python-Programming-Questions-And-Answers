'''
There are various ways in which the difference between two lists can be generated. 
In this article, we will see the two most important ways in which this can be done. 
One by using the set() method, and another by not using it. 
 

Examples:  

Input :
list1 = [10, 15, 20, 25, 30, 35, 40]
list2 = [25, 40, 35] 
Output :
[10, 20, 30, 15]
Explanation:
resultant list = list1 - list2
          
 Note: When you have multiple same elements then this would not work. 
 In that case, this code will simply remove the same elements.
In that case, you can maintain a count of each element in both lists.
'''
list2 = [10, 15, 20, 25, 30, 35, 40]
list1 = [25, 40, 35] 

l1 = len(list1)
l2 = len(list2)
if l1 > l2:
    print(set(list1).difference(set(list2)))
else:
    print(set(list2).difference(set(list1)))


# Brute Way
list2 = [10, 15, 20, 25, 30, 35, 40]
list1 = [25, 40, 35] 

l1 = len(list1)
l2 = len(list2)
if l1 > l2:
    for x in list2:
        if x in list1:
            list1.remove(x)
    print(list1)
else:
    for x in list1:
        if x in list2:
            list2.remove(x)
    print(list2)