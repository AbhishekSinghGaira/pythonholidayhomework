''' Python script to generate and print a dictionary that contains a number (between 1 and n) in the form (x, x*x). '''
n = int(input("Enter a number: "))

result = {}
for x in range(1, n+1):
    result[x] = x * x

print("Generated dictionary:")
print(result)
