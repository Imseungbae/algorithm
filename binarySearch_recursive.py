#재귀로 이진탐색 구현하기
def binarySerch(arr, target, start, end):

    while start <= end:
        mid = (start+end)//2

        if target == arr[mid]:
            print(mid)
            return mid
        elif target < arr[mid]:
            return binarySerch(arr, target, start, mid-1)
        else :
            return binarySerch(arr, target, mid+1, end)
        


arr = [2,4,6,8,10,12,14,16,18]
target = 8

print(binarySerch(arr, target, 0, len(arr)-1))