arr = [7,5,9,0,3,1,6,2,9,1,4,8,0,5,2]

def countSort(arr):
    maxValue = max(arr)
    countList = [0] * (maxValue + 1)

    for i in arr:
        countList[i] += 1

    for i in range(len(countList)):
        for _ in range(countList[i]):
            print(i, end=' ')

countSort(arr)
