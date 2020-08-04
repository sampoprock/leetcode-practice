# Given an array arr[] of N non-negative integers representing height of blocks at index i as Ai where the width of each block is 1. Compute how much water can be trapped in between blocks after raining.
# Structure is like below:
# |  |
# |_|
# We can trap 2 units of water in the middle gap.



# Input:
# The first line of input contains an integer T denoting the number of test cases. The description of T test cases follows. Each test case contains an integer N denoting the size of the array, followed by N space separated numbers to be stored in array.

# Output:
# Output the total unit of water trapped in between the blocks.

# Constraints:
# 1 <= T <= 100
# 3 <= N <= 107
# 0 <= Ai <= 108

# Example:
# Input:
# 2
# 4
# 7 4 0 9
# 3
# 6 9 9

# Output:
# 10
# 0

# Explanation:
# Testcase 1: Water trapped by block of height 4 is 3 units, block of height 0 is 7 units. So, total unit of water trapped is 10 units.










#code
n=int(input())
for _ in range(n):
    size=int(input())
    arr=list(map(int,input().strip().split(" ")))
    arr1=[]
    arr2=[]
    water=0
    m=arr[0]
    for i in arr:
        if i>m:
            m=i
        arr1.append(m)
    temp=arr
    temp.reverse()
    m=temp[0]
    for i in temp:
        if i>m:
            m=i
        arr2.append(m)
    arr2.reverse()
    for i in range(len(arr)):
        water+=min(arr1[i],arr2[i])-arr[i]
    print(water)