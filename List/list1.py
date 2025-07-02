#Intersection on two sets
Seta= eval(input("Enter the first set --->"))
Setb= eval(input("Enter the second set --->"))

intersection=[]

for i in Seta:
    if i in Setb:
        intersection.append(i)
    else:
        pass

print(f'The common elemnts of setA and setB is {intersection}')