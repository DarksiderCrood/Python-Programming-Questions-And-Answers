'''
Given a list, dictionary and a Key K, print value of K from dictionary if 
key present in both, list and dictionary.

Input : test_list = [“Gfg”, “is”, “Good”, “for”, “Geeks”], test_dict = {“Gfg” : 5, “Best” : 6}, K = “Gfg”
Output : 5
Explanation : “Gfg” is present in list and has value 5 in dictionary.

Input : test_list = [“Good”, “for”, “Geeks”], test_dict = {“Gfg” : 5, “Best” : 6}, K = “Gfg”
Output : None
Explanation : “Gfg” not present in List.
'''

test_list = ["Gfg", "is", "Good", "for", "Geeks"]
test_dict = {"Gfg" : 5, "Best" : 6}
K = "Gfg"


if K in test_list and test_dict:
    print(test_dict["Gfg"])