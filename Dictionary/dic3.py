'''Python script to sort (ascending and descending) a dictionary by value. '''

my_dict = {'apple': 3, 'banana': 1, 'cherry': 5, 'date': 2}

asc_sorted = dict(sorted(my_dict.items(), key=lambda item: item[1]))
print("Ascending sort by value:")
print(asc_sorted)

desc_sorted = dict(sorted(my_dict.items(), key=lambda item: item[1], reverse=True))
print("Descending sort by value:")
print(desc_sorted)
