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

# Exercise 9: Given a Python list, find value 20 in the list, and if it is present, replace it with 200. Only update the first occurrence of a value
'''list1 = [5, 20, 15, 20, 25, 50, 40,20]
count = 0
for x in range(0, len(list1)):
    if count<1 and list1[x]==20:
        count+=1
        list1[x]=200
print(list1)

index = list1.index(20)
list1[index] = 200
print(list1)'''

# Exercise 10: Given a Python list, remove all occurrence of 20 from the list
'''list1 = [5, 20, 15, 20, 25, 50, 20]
list2 = [x for x in list1 if x!=20]
print(list2)'''

# 1. Write a python program to find the sum of all numbers in a list
'''l = [1,2,3,4,5,6,7,8,9,10]
print(sum(l))
# or
sums = 0
for x in l:
    sums+=x
print(sums)'''

# 2. Write a python program to find largest number in a given list with out using max()
'''l = [3,6,1,3,8,9,3,4,5,6,9,1,3,5]
print(max(l)) # with max
# or
l.sort()
print(l[len(l)-1]) # with sort and len
# or
max = 0
for x in l:
    if x > max:
        max = x
print(max)'''

# 3. Write a python program to find the common numbers from two lists
'''q = [1,3,5,7,9]
w = [0,3,5,7,11]
for x,y in zip(q,w):
    if x == y:
        print("Common Numbers are: ", x)
# or
a, s = set(q), set(w)
print(a.intersection(s))'''

# 4. Write a python program to print all even numbers from a given list
'''l = [1,2,3,4,5,6,7,8,9,10]
print([x for x in l if x%2==0])'''

# 5. Write a python program to create a list of even numbers and another list of odd numbers from a given list
'''l = [1,2,3,4,5,6,7,8,9,10]
print([x for x in l if x%2==0])
print([x for x in l if x%2!=0])'''

# 6. Write a python program to remove repeated elements from a given list without using built-in methods
'''l = [1,2,3,3,4,5,5,5,6,7,8,8,9,0,0]
n = []
for x in l:
    if x not in n:
        n.append(x)
print(n)'''

# 7. Write a python program to find the longest word in a given sentence
'''l = ['qwe','asdff','DFDSFDg','zxcvxcvx','sdfsdfs']
print(max(l))
# or
max = 0
word = ''
for x in l:
    if len(x) > max:
        max = len(x)
        word = x
print(word, max)'''

# 8. Write a python program to find number of occurrences of given number with out using built-in methods
'''l = [1,2,3,3,4,5,5,5,6,7,8,8,9,0,0]
n = 5
c = 0
for x in l:
    if x == n:
        c+=1
print(n,"comes in list {} times".format(c))'''

# 9. ["www.zframez.com", "www.wikipedia.org", "www.asp.net", "www.abcd.in"]
# Write a python program to print website suffixes (com , org , net ,in) from this list
'''l = ["www.zframez.com", "www.wikipedia.org", "www.asp.net", "www.abcd.in"]
for x in l:
    print(x.split('.')[2])'''

# 10. Write a python program to sort a given list of numbers with out using sort() function
def bubbleSort(arr):
	n = len(arr)

	# Traverse through all array elements
	for i in range(n):
		swapped = False

		# Last i elements are already
		# in place
		for j in range(0, n-i-1):

			# traverse the array from 0 to
			# n-i-1. Swap if the element
			# found is greater than the
			# next element
			if arr[j] > arr[j+1] :
				arr[j], arr[j+1] = arr[j+1], arr[j]
				swapped = True

		# IF no two elements were swapped
		# by inner loop, then break
		if swapped == False:
			break
		
# Driver code to test above
arr = [64, 34, 25, 12, 22, 11, 90]

bubbleSort(arr)

print ("Sorted array :")
for i in range(len(arr)):
	print ("%d" %arr[i],end=" ")