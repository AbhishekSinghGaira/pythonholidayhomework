'''Python program to filter the height and width of students, which are stored in a dictionary. '''

# Sample data
students = {
    'Amit': {'height': 165, 'weight': 55},
    'Ravi': {'height': 172, 'weight': 70},
    'Neha': {'height': 160, 'weight': 48},
    'Priya': {'height': 168, 'weight': 60}
}

for name in students:
    h = students[name]['height']
    w = students[name]['weight']
    
    if h > 165 and w < 65:
        print(name, "=> Height:", h, "Weight:", w)
