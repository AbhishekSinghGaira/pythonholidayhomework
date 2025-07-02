'''Python program to combine two dictionary by adding values for common keys. '''
# Sample dictionaries
dict1 = {'a': 100, 'b': 200, 'c': 300}
dict2 = {'a': 300, 'b': 200, 'd': 400}

# Final combined dictionary
result = {}

# Add values from first dictionary
for key in dict1:
    result[key] = dict1[key]

# Add values from second dictionary
for key in dict2:
    if key in result:
        result[key] += dict2[key]  # add if key already exists
    else:
        result[key] = dict2[key]   # else just set it

print("Combined dictionary:")
print(result)
