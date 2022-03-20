arr = [0,2,4,8,10,12,14,16,18]

target = int(input())

def binarySearch(str, end):
    if str > end:
        return -1

    mid = (str+end)//2

    if target == arr[mid]:
        return mid
    elif target < arr[mid]:
        binarySearch(str, mid-1)
    else :
        binarySearch(mid+1, end)

# binarySearch(0, len(arr)-1)

def binarySearch2(target):
    str = 0
    end = len(arr)-1

    while str > end:
        mid = (str+end)//2
        if target == arr[mid]:
            print("find!!!")
            break
        elif target < arr[mid]:
            end = mid -1
        else :
            str = mid +1
binarySearch2(target)
