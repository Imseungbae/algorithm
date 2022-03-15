import sys
input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())
dist = [[ INF for _ in range(n+1)] for _ in range(n+1)] 

for i in range(n+1):
    dist[i][i] = 0

for _ in range(m):
    a,b = map(int, input().split())
    dist[a][b] = 1
    dist[b][a] = 1

x, k = map(int, input().split())

def ployed():
    for i in range(1, n+1):
        for j in range(1, n+1):
            for k in range(1, n+1):
                dist[j][k] = min(dist[j][i]+dist[i][k], dist[j][k])
ployed()
print(dist[1][k] + dist[k][x])

'''
5 7
1 2
1 3
1 4
2 4
3 4
3 5
4 5
4 5
'''