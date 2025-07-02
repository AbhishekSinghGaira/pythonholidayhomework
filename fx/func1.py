'''pascals triangle'''

def pascal_row(n):
    row = []
    val = 1  # C(n, 0) = 1
    for k in range(n + 1):
        row.append(val)
        val = val * (n - k) // (k + 1)
    return row

n = int(input("Enter the row number (0-based): "))
result = pascal_row(n)
print("Pascal's Triangle Row", n, ":", result)
