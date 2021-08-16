# Exercise 1: Reverse the following tuple
q1 = ("A", 1, "B", 2, "C", 3)
q2 = ("Geek1", "Raju", "Geek2", "Nikhil", "Geek3", "Deepanshu")
q3 = ((1, "Lion"), ( 2, "Tiger"), (3, "Fox"), (4, "Wolf"))
print(q1[::-1])
w1 = reversed(q1)
print(tuple(w1))

# Exercise 2: Access value 20 from the following tuple
q1 = ("Orange", [10, 20, 30], (5, 15, 25))
print(q1[1][1])

# Exercise 3: Create a tuple with single item 50 and a tuple with 50 items
tu = (x for x in range(1,51))
print(tuple(tu))
we = (50, )
print(we)

# Exercise 5: Swap the following two tuples
qw = (11, 22)
wq = (99, 88)
print("Before Swap")
print("QW:", qw,"WQ:", wq)
temp = ()
temp = qw
qw = wq
wq = temp
print("After Swap")
print("QW:", qw,"WQ:", wq)
qw, wq = wq, qw
print("Swap Again")
print("QW:", qw,"WQ:", wq)