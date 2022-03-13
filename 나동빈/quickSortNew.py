arr = [5,7,9,0,3,1,6,2,4,8]

def quickSort(list):

    if len(list)<=1:
        return list

    pivot = list[0]
    arr = list[1:]

    left = [x for x in arr if x < pivot]
    right = [x for x in arr if x > pivot]

    return quickSort(left) + [pivot] + quickSort(right)


print(quickSort(arr))