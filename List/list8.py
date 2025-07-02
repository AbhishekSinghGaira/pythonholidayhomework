#You are given a list arr that contains integers. You need to count distinct integers in list. 

arr=eval(input("enter the number"))
distinct_count = len(set(arr))
print("Number of distinct elements:", distinct_count)