arr = [5,7,9,0,3,1,6,2,4,8]

def quickSort(str, end):
    if str >= end :
        return 

    pivot = str
    left = str + 1
    right = end

    while left < right:
        while left <= end and arr[pivot] > arr[left] :
            left += 1
        while right > pivot and arr[pivot] < arr[right]:
            right -= 1
        if left < right :
            arr[left], arr[right] = arr[right], arr[left]
        else :
            arr[right], arr[pivot] = arr[pivot], arr[right]
    
    quickSort(str, right-1)
    quickSort(right+1, end)
    return


quickSort(0, len(arr)-1)
print(arr)