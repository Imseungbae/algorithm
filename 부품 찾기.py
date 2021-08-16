# binarySearch이용
# import sys

# N = int(input())
# listN = list(map(int,input().split()))


# M = int(input())
# listM = list(map(int,input().split()))

# def binarySearch(arr, target, start, end):
#     if start > end:
#         return None
#     mid = (start+end)//2
#     if arr[mid] == target:
#         return mid
#     elif arr[mid] > target:
#         return binarySearch(arr, target, start, mid-1)
#     else :
#         return binarySearch(arr, target, mid+1, end)

# # print(binarySearch(listN,5,0,len(listN)-1))

# listN.sort()

# for target in listM:
#     if binarySearch(listN, target, 0, len(listN)-1) is not None:
#         print("yes")
#     else:
#         print("no")

# 2.countSort 이용
# N = int(input())
# listN = list(map(int,input().split()))

# M = int(input())
# listM = list(map(int,input().split()))

# count = [0] * (max(listN)+1)

# for i in listN:
#     count[i] += 1

# for i in listM:
#     if count[i] >0 :
#         print("yes")
#     else :
#         print("no")


# print(count)

# 3. set 이용
N = int(input())
array = set(map(int,input().split()))
M = int(input())
listM = list(map(int,input().split()))

for i in listM:
    if i in array:
        print("yes")
    else :
        print("No")