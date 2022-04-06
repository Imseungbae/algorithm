n = int(input())

arr = [1,2,3,4,5]

if n >= len(arr):
    n = n%len(arr)
    
print(arr[n])
