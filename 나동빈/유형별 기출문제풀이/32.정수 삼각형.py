from copy import deepcopy
from turtle import right

n = int(input())
a = []

for _ in range(n):
    a.append(list(map(int, input().split())))

dp = deepcopy(a)

for i in range(n):
    for j in range(0, i+1):
        print(i, " ", j)
        if j == 0 :
            leftVal = 0
        else :
            leftVal = dp[i-1][j-1]
        if j == i:
            rightVal = 0
        else :
            rightVal = dp[i-1][j]
        dp[i][j] = a[i][j] + max(leftVal, rightVal)
        
result = 0
for i in range(n):
    result = max(dp[n-1][i], result)

print(result)
    
'''
5
7
3 8
8 1 0
2 7 4 4
4 5 2 6 5
'''