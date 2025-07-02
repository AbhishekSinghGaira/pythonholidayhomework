'''There are n children standing in a line. Each child is assigned a rating value given in the integer array arr[]. You are giving candies to these children subjected to the following requirements:

    Each child must have at least one candy.
    Children with a higher rating than their neighbors get more candies than their neighbors.

Return the minimum number of candies you need to have to distribute.'''

arr = eval(input("Enter ratings of children: "))
n = len(arr)

candies = [1] * n  # step 1: sabko 1 candy de do

# step 2: left to right
for i in range(1, n):
    if arr[i] > arr[i-1]:
        candies[i] = candies[i-1] + 1

# step 3: right to left
for i in range(n-2, -1, -1):
    if arr[i] > arr[i+1]:
        candies[i] = max(candies[i], candies[i+1] + 1)

# step 4: total
print("Minimum candies required:", sum(candies))
