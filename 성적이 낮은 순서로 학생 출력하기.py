n = int(input())
arr = []

for _ in range(n):
    x = input().split()
    arr.append(x)
arr.sort(key = lambda x:x[1])

for i in arr:
    print(i[0], end=' ')