'''
Reverse All Strings in String List in Python
'''

a = ["apple", "banana", "cherry", "date"]

res = []

for s in a:
    res.append(s[::-1])

print(res)