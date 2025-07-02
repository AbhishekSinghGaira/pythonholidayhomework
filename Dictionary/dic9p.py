'''	Match Key Values in Two Dictionaries'''

dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'a': 1, 'b': 5, 'd': 3}

for key in dict1:
    if key in dict2 and dict1[key] == dict2[key]:
        print("Matching key-value pair:", key, ":", dict1[key])
