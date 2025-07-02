#You are given an array arr[] of non-negative integers. Your task is to move all the zeros in the array to the right end while maintaining the relative order of the non-zero elements. The operation must be performed in place, meaning you should not use extra space for another array.

arr = eval(input("Enter the array: "))

non_zero_index = 0

for i in range(len(arr)):
    if arr[i] != 0:
        arr[non_zero_index] = arr[i]
        non_zero_index += 1

for i in range(non_zero_index, len(arr)):
    arr[i] = 0

print("Modified Array:", arr)
