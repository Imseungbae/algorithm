#이진탐색 구현 O(logN)
arr = [0,2,4,6,8,10,12,14,16,18]
target =14


start = 0
end = len(arr)-1

while start <= end:
    mid = (start+end)//2

    if target == arr[mid]:
        print("find!!",arr[mid])
        break
    elif target < mid:
        print("왼쪽탐색")
        end = mid - 1
    else :
        start = mid + 1
        print("오른쪽탐색")