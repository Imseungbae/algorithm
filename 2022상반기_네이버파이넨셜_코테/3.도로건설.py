from itertools import product

n, m, k = map(int, input().split())

arr = [x for x in range(1, k+1)]

array = list(product(arr,repeat=n))
cnt = 0

for i in array:
    if sum(i) == m:
        cnt += 1
        print(i)

print(cnt)