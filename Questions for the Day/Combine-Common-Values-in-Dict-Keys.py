'''
Implement a group_by_owners function that:
• Accepts a dictionary containing the file owner name for each file name.
• Returns a dictionary containing a list of file names for each owner
name, in any order.

For example, for dictionary
['Input.txt': 'Randy', 'Code.py': 'Stan', 'Output.txt': 'Randy'}
the group_by_owners function should return
{'Randy': ['Input.txt', 'Output.txt'], 'Stan': ['Code.py']}
'''

inp_dict = {'Input.txt': 'Randy','Code.py': 'Stan','Output.txt': 'Randy'}
output = {}
for file, owner in inp_dict.items():
    output[owner] = output.get(owner, []) + [file]
print (output)