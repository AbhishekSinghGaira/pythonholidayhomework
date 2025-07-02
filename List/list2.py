#Union of the two sets


Seta= eval(input("Enter the first set --->"))
Setb= eval(input("Enter the second set --->"))
a= list(Setb)

for i in Seta:
    if i in Setb:
        continue
    else:
        a.append(i)

print(f'The common elemnts of setA and setB is {a}')