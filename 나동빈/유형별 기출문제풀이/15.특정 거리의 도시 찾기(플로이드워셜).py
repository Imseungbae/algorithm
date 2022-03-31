'''
4 4 2 1
1 2
1 3
2 3
2 4

간선 추가 입력
4 4 2 1
1 2 1
1 3 1
2 3 1
2 4 1
'''

import sys
input = sys.stdin.readline
INF = int(1e9)

n, m, k, x = map(int, input().split())
graph = [[] for _ in range(n+1)]

# distance 이차원배열
# O(n^3)
distance = [[INF for _ in range(n+1)] for _ in range(n+1)]

for _ in range(m):
    a,b,c = map(int, input().split())
    graph[a].append((b,c))
    distance[a][b] = c
    
for i in range(len(distance)):
    distance[i][i] = 0

def FloydWarshall(distance):
    for i in range(n+1):
        for j in range(n+1):
            for k in range(n+1):
                distance[i][j] = min(distance[i][j], distance[i][k] + distance[k][j])


FloydWarshall(distance)

for i in range(len(distance[x])):
    if k == distance[x][i]:
        print(i)


