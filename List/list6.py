#Given an unsorted array arr containing both positive and negative numbers. Your task is to rearrange the array and convert it into an array of alternate positive and negative numbers without changing the relative order.


arr = eval(input("Enter the numbers: "))

pos = []
neg = []
for num in arr:
    if num >= 0:
        pos.append(num)
    else:
        neg.append(num)

start_with_pos = True if arr[0] >= 0 else False

i = j = k = 0
result = []

while i < len(pos) and j < len(neg):
    if start_with_pos:
        result.append(pos[i])
        result.append(neg[j])
    else:
        result.append(neg[j])
        result.append(pos[i])
    i += 1
    j += 1

# Remaining elements
while i < len(pos):
    result.append(pos[i])
    i += 1
while j < len(neg):
    result.append(neg[j])
    j += 1

print("Rearranged Array:", result)
