arr = list(map(int, input()))

mid = len(arr)//2

first = sum(arr[:mid])
second = sum(arr[mid:])

if first == second:
    print("LUCKY")
else :
    print("READY")