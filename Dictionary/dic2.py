'''
Python - Dictionary Values Mean
'''


test_dict = {"Gfg" : 4, "is" : 7, "Best" : 8, "for" : 6, "Geeks" : 10}

print("The original dictionary is : " + str(test_dict))

res = 0
for val in test_dict.values():
    res += val

res = res / len(test_dict)

# printing result 
print("The computed mean : " + str(res))