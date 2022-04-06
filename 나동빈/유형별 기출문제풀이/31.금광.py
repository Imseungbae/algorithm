t = int(input())
n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr2 = []
dp = [ [0 for i in range(m+1)] for i in range(n+1)]
for i in arr:
    cnt = 0
    temp = []
    while True:
        cnt +=1
        temp.append(arr.pop(0))

        if cnt == 4:
            arr2.append(temp)
            break


for j in range(m):
    for i in range(n):
        a = arr2[i][j]
        b1 = dp[i-1][j-1]
        b2 = dp[i][j-1]
        b3 = dp[i+1][j-1]
        dp[i][j] = a + max(b1, b2, b3)

print(arr2)
print(dp)
_max = 0
for i in dp:
    temp = max(i)
    if temp > _max:
        _max = temp

print(_max)

'''
2
3 4
1 3 3 2 2 1 4 1 0 6 4 7
1
4 4
1 3 1 5 2 2 4 1 5 0 2 3 0 6 1 2
'''