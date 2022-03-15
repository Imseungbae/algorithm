import sys
input = sys.stdin.readline
INF = int(1e9)

n = int(input())
m = int(input())

dist = [[INF for _ in range(n+1)] for _ in range(n+1)]

for _ in range(m):
    a,b,c = map(int, input().split())
    dist[a][b] = c

for i in range(n+1):
    dist[i][i] = 0

def ployed():
    for i in range(1, n+1):
        for j in range(1, n+1):
            for k in range(1, n+1):
                dist[j][k] = min(dist[j][k], dist[j][i] + dist[i][k])
ployed()
print(dist)

'''
4
7
1 2 4
1 4 6
2 1 3
2 3 7
3 1 5
3 4 4
4 3 2
'''