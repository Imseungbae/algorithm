N, M = map(int,input().split())
coins=[]
for _ in range(N):
    coins.append(int(input()))

dp = [10001] * 101


#bottom Up
dp[0] = 0
for i in coins:
    dp[i] = i
    
for i in range(N):
    for j in range(coins[i], M+1):
        dp[j] = min(dp[j], dp[j - coins[i]]+1)


if (dp[M] == 10001):
    print(-1)
else:
    print(dp[M])