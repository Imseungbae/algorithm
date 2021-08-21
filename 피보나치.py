# #1. 재귀이용

# def pibo(n):
#     if n==1 or n==2:
#         return 1
#     return pibo(n-1) + pibo(n-2)

# #2. Top-Down 방식 이용
# d = [0] * 101

# def pibo(n):
#     print("f(",n,")")
#     if n ==1 or n ==2 :
#         return 1
#     if d[n] != 0:
#         return d[n]
    
#     d[n] = pibo(n-1) + pibo(n-2)
#     return d[n]

# pibo(6)

# #. Bottom-Up 방식 이용

# dp = [0] * 101
# dp[1] = 1
# dp[2] = 1

# for n in range(3, 101):
#     dp[n] = dp[n-1] + dp[n-2]
# print(dp[100])






#Top Down방식 이용
d = [0] * 100

def pibo(X):
    print("f(",X,")")
    if X == 1 or X == 2:
        return 1
    
    if d[X] != 0 :
        return d[X]
    
    d[X] = pibo(X-1) + pibo(X-2)
    return d[X]

print(pibo(6))


#Bottom UP 방식
dp = [0] * 100

dp[1] = 1
dp[2] = 1

for i in range(3, 100):
    dp[i] = dp[i-1] + dp[i-2]

print(dp[10])