'''
Get Values of Particular Key in List of Dictionaries - Python
'''

li = [{'aryan': 10, 'harsh': 20}, {'aryan': 30, 'kunal': 40}, {'harsh': 50}]
k = 'aryan'
res = [d.get(k) for d in li if k in d]
print(res)