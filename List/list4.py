#To find relation from set A to set B
setA = [1]
setB = [2, 3]

relation = []

for a in setA:
    for b in setB:
        relation.append((a, b))  # adding tuple to the list

print("Relation from A to B:")
print(relation)

