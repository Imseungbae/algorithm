'''
7
0110100
0110101
1110101
0000111
0100000
0111110
0111001
'''

n = int(input())
arr = []

# 북동남서
dx = [-1,0,1,0]
dy = [0,1,0,-1]

# 2차원 배열 입력
for i in range(n):
    arr.append( list(map(int, input())) )
cnt = 0
def dfs(x, y):
    global cnt
    cnt += 1
    arr[x][y] = 2
    for i in range(4):
        rx = x + dx[i]
        ry = y + dy[i]

        if rx < 0 or ry < 0 or rx >= n or ry >= n:
            continue

        if arr[rx][ry] == 1:
            dfs(rx, ry)
    return cnt

result = []
totCnt = 0
# (0,0)부터 순차적으로 방문
for i in range(n):
    for j in range(n):
        if arr[i][j] == 1:
            result.append(dfs(i, j))
            totCnt += 1
            cnt = 0


print(totCnt)

for i in sorted(result):
    print(i)