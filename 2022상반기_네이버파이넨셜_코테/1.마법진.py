from copy import deepcopy
from itertools import combinations

arr = [1,2,1,2,1,2,1,2,1]

def solution():
    if sum(arr)%3 != 0:
        return 0
    
    target = sum(arr)//3

    arr2 =[]
    arr4 = []
    for i in list(combinations(arr, 3)):
        if sum(i) == target:
            arr2.append(i)

    print("arr2: ", arr2)

    for i in arr2:
        # arr3 = [x for x in arr if x not in i]
        arr3 = deepcopy(arr)

        for i2 in i:
            if i2 in arr3:
                arr3.remove(i2)
        

        for j in list(combinations(arr3, 3)):
            if sum(j) == target:
                arr4.append(j)
                print(i, j)

                # arr5 = [x for x in arr if x not in i and x not in j]

                for i3 in j:
                    if i3 in arr3:
                        arr3.remove(i3)

                arr5 = arr3
                print(arr5)
                if sum(arr5) == target:
                    print(i,j,arr5)
                    return 1
    return 0

print( solution() )
