#1. 재귀이용

def pibo(n):
    if n==1 or n==2:
        return 1
    return pibo(n-1) + pibo(n-2)

#2. Top-Down 방식 이용
d = [0] * 101

def pibo(n):
    print("f(",n,")")
    if n ==1 or n ==2 :
        return 1
    if d[n] != 0:
        return d[n]
    
    d[n] = pibo(n-1) + pibo(n-2)
    return d[n]

pibo(6)

#. Bottom-Up 방식 이용

dp = [0] * 101
dp[1] = 1
dp[2] = 1

for n in range(3, 101):
    dp[n] = dp[n-1] + dp[n-2]
print(dp[100])


