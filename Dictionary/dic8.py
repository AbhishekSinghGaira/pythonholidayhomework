'''	Combinations of Letters from Dictionary Keys'''
my_dict = {'a': 1, 'b': 2, 'c': 3}

keys = list(my_dict.keys())

combinations = []

n = len(keys)

i = 1
while i < (1 << n):
    combo = ""
    j = 0
    while j < n:
        if i & (1 << j):
            combo += keys[j]
        j += 1
    combinations.append(combo)
    i += 1

for combo in combinations:
    print(combo)

