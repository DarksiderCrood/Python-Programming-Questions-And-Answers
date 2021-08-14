# Exercise 1: Below are the two lists convert it into the dictionary
'''keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]
dic = {x:y for x,y in zip(keys,values)}
Dict = dict(zip(keys, values))
print(dic)
print(Dict)'''

# Exercise 2: Merge following two Python dictionaries into one
# Expected output: {'Ten': 10, 'Twenty': 20, 'Thirty': 30, 'Fourty': 40, 'Fifty': 50}
'''dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}
dict1.update(dict2)
print(dict1)
dict3 = {**dict1, **dict2}
print(dict3)'''

# Exercise 3: Access the value of key ‘history’ from the below dict
'''sampleDict = { 
   "class":{ 
      "student":{ 
         "name":"Mike",
         "marks":{ 
            "physics":70,
            "history":80
         }
      }
   }
}
print(sampleDict['class']['student']['marks']['history'])'''

# Exercise 4: Initialize dictionary with default values
'''employees = ['Kelly', 'Emma', 'John']
defaults = {"designation": 'Application Developer', "salary": 8000}
Dict = dict.fromkeys(employees, defaults)
print(Dict)'''

# Ref: for more https://pynative.com/python-dictionary-exercise-with-solutions/