N,M = map(int,input().split())
arr = list(map(int,input().split()))
arr.sort

start = 0
end = max(arr)


# while start < end:
#     tempSum = 0
#     mid = (start+end)//2
#     for i in arr:
#         if i > mid:
#             tempSum += i-mid
    
#     if tempSum < M:
#         end = mid -1
#     else:
#         result = mid
#         start = mid + 1
result = 0

def binary(arr, M, start , end, result):
    target = 0
    mid = (start+end)//2
    print(start, end)
    if start >= end:
        return result

    for i in arr:
        if i > mid:
            target += i - mid
    if target < M:
        return binary(arr, M, start, mid-1, result)
    else :
        result = mid
        return binary(arr,M, mid+1, end, result)

print(binary(arr,M,start,end, 0))