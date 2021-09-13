'''
Given two Strings, separated by delim, check if both contain same characters.

Input : test_str1 = ‘e!e!k!s!g’, test_str2 = ‘g!e!e!k!s’, delim = ‘!’
Output : True
Explanation : Same characters, just diff. positions.

Input : test_str1 = ‘e!e!k!s’, test_str2 = ‘g!e!e!k!s’, delim = ‘!’
Output : False
Explanation : g missing in 1st String.
'''

from typing_extensions import TypeGuard


test_str1 = 'e!e!k!s!g'
test_str2 = 'g!e!e!k!s'
delim = '!'
test_str1 = sorted(test_str1.split('!'),reverse=True)
test_str2 = sorted(test_str2.split('!'),reverse=True)
print(test_str1, test_str2)