from copy import deepcopy


n = int(input())
arr = []
for _ in range(n):
    arr.append(int(input()))

# 난이도 ★★☆☆☆
def selectSort(arr): 
    for i in range(len(arr)):
        minIdx = i

        for j in range(i+1, len(arr)):
            if arr[minIdx] > arr[j]:
                minIdx = j

        arr[minIdx], arr[i] = arr[i], arr[minIdx]

# 난이도 ★★★☆☆
def insertSort(arr):
    for i in range(1, len(arr)):
        j = i - 1

        while j >= 0:
            if arr[j] > arr[i]:
                arr[j], arr[i] = arr[i], arr[j]
                i=j
            j -= 1

def insertSortII():
    global arr
    for i in range(1, len(arr)):
        for j in range(i,0,-1):
            if arr[j-1] > arr[j]:
                arr[j-1], arr[j] = arr[j], arr[j-1]
             


# 난이도 ★★☆☆☆
def bubbleSort(arr):
    for i in range(len(arr)):
        print(str(i) ,"번 시행 : " , arr)

        for j in range(len(arr)-i):
            if j == len(arr)-1:
                continue
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

def bubbleSortII():
    global arr
    for i in range(len(arr)-1,0,-1):
        for j in range(i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

# 난이도 ★★★☆☆
def quickSort(arr):

    if len(arr) < 1:
        return []

    pivot = 0
    tail = arr[1:]

    left = [x for x in tail if x < arr[pivot]]
    right = [x for x in tail if x >= arr[pivot]]

    return quickSort(left) + [arr[pivot]] + quickSort(right)
    

# 난이도 ★☆☆☆☆
def countSort():
    global arr
    countArr = [0] * (max(arr)+1)
    for i in arr:
        countArr[i] += 1
    arr = countArr
    
    for i in range(len(arr)):
        if arr[i] > 0:
            print(i, end = " ")


# insertSortII()
bubbleSortII()
print(arr)