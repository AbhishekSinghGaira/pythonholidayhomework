'''Python program to sort a given dictionary by key. '''
my_dict = {'banana': 3, 'apple': 5, 'cherry': 2, 'date': 4}

sorted_dict = dict(sorted(my_dict.items()))

print("Dictionary sorted by key:")
print(sorted_dict)
