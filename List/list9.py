arr = eval(input("Enter binary array: "))

ones = arr.count(1)

if ones == 0:
    print(-1)
else:
    window_size = ones
    current_zeros = 0

    # count zeros in first window
    for i in range(window_size):
        if arr[i] == 0:
            current_zeros += 1

    min_swaps = current_zeros

    # sliding window
    for i in range(window_size, len(arr)):
        if arr[i - window_size] == 0:
            current_zeros -= 1
        if arr[i] == 0:
            current_zeros += 1
        if current_zeros < min_swaps:
            min_swaps = current_zeros

    print("Minimum swaps to group all 1s:", min_swaps)
