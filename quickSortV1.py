array = [5,7,9,0,3,1,6,2,4,8]

def quick(array, start, end):
    if start >= end :
        return

    pivot = start
    L = start + 1
    R = end
    
    while R > L :
        while L <= R and array[pivot] > array[L]:
            L += 1
        while R >= L and array[pivot] < array[R]:
            R -= 1

        # swap
        if L > R:
             array[pivot], array[R] =  array[R],array[pivot]
        # pivot swap
        else : 
            array[L], array[R] =  array[R], array[L] 
    quick(array, start, R-1)
    quick(array, R+1, end)

quick(array, 0, len(array)-1)
print(array)