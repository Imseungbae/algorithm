#select_sort implementation

array = [7,5,9,0,3,1,6,2,4,8]

for i in range(len(array)):
    minIdx = i
    for j in range(i+1, len(array)):
        #여기서 최소값 구한다
        if array[minIdx] > array[j]:
            minIdx = j
    #여기서 min값이랑 i랑 스왑한다
    array[i], array[minIdx] = array[minIdx], array[i]
    

print(array)
array.reverse()
print(array)
# for i in range(len(array)):
#     for j in range(len(array)-i):