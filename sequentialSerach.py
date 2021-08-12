#순차탐색
N, target = input().split()
arr = list(input().split())

#탐색시작
for i in range(len(arr)):
    if target == arr[i]:
        print(i+1)