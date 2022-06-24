n = int(input())
d = [-1] * (n+1)

# 재귀이용
def recur(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    
    if d[n] != -1:
        return d[n]

    d[n] = recur(n-1) + recur(n-2)
    return d[n]

#dp 보텀업
def bottomUp(n):
    dp = [0] * (n+1)

    if n == 0:
        return 0
    if n == 1:
        return 1
    
    dp[0] = 0
    dp[1] = 1

    for i in range(2, n+1):
        dp[i] = dp[i-1] + dp[i-2]
    
    return dp[n]

print( recur(n) )
print( bottomUp(n) )