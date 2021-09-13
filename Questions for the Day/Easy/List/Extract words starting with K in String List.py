'''
Given list of phrases, extract all the Strings with begin with character K.

Input : test_list = [“Gfg is good for learning”, “Gfg is for geeks”, “I love G4G”], K = l
Output : [‘learning’, ‘love’]
Explanation : All elements with L as starting letter are extracted.

Input : test_list = [“Gfg is good for learning”, “Gfg is for geeks”, “I love G4G”], K = m
Output : []
Explanation : No words started from “m” hence no word extracted.
'''

test_list = ['the final word kill', 'will not knight you', 'until you know him', 'for right kind']
K = 'k'

l = [x.split(' ') for x in test_list]
test_list = []
for x in l:
    for y in x:
        if y[0] == K:
            test_list.append(y)
print(test_list)