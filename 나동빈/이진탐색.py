arr = [1,2,4,5,6,7,8,9,10]

def binarySearch(target, str, end):
    if str > end :
        return -1

    mid = (str+end)//2

    if arr[mid]== target:
        print(target)
        return target
    elif arr[mid] < target:
        binarySearch(target, mid+1, end)
    elif arr[mid] > target:
        binarySearch(target, str, mid-1)

binarySearch(2, 0, len(arr)-1)