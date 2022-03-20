arr = [7,5,9,0,3,1,6,2,9,1,4,8,0,5,2]
arr2 = [1,7,5,9,4,2,3,11]
arr = arr2
# def countSort(arr):
#     maxValue = max(arr)
#     countList = [0] * (maxValue + 1)

#     for i in arr:
#         countList[i] += 1

#     for i in range(len(countList)):
#         for _ in range(countList[i]):
#             print(i, end=' ')

# countSort(arr)



countArr = [0] * (max(arr) + 1)

def countSort(arr):
    for i in arr:
        countArr[i] += 1

countSort(arr)
for i in range(len(countArr)):
    if countArr[i] > 0:
        print(i, end=" ")