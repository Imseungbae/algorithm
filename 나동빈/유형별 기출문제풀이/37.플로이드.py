n = int(input())
m = int(input())
INF = int(1e9)

graph = [[INF for i in range(n+1)] for i in range(n+1)]

for _ in range(m):
    a,b,c = map(int, input().split())
    if graph[a][b] > c:
        graph[a][b] = c

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            old = graph[i][j]
            new = graph[i][k] + graph[k][j]
            graph[i][j] = min(old, new)

for i in range(1, n+1):
    graph[i][i] = 0

for i in range(1, n+1):
    print(graph[i][1:])


'''
5
14
1 2 2
1 3 3
1 4 1
1 5 10
2 4 2
3 4 1
3 5 1
4 5 3
3 5 10
3 1 8
1 4 2
5 1 7
3 4 2
5 2 4
'''