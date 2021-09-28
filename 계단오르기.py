n = int(input())
score =[0] * 301
for i in range(n):
    score[i+1] = int(input())

dp = [0] * 301
dp[1] = score[1]
dp[2] = dp[1] + score[2]

for i in range(3, n+1):
    dp[i] =  max(score[i] + score[i-1] + dp[i-3], score[i] + dp[i-2])

print(dp[n])