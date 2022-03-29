'''
[[[[[[[[[[입력값]]]]]]]]]
8 9
2 3 8
1 7
1 4 5
3 5
3 4
7
2 6 8
1 7
[[[[[[[[[출력값]]]]]]]]]
1 2 7 6 8 3 4 5 
'''


import sys
input = sys.stdin.readline
INF = int(1e9)

v, e = map(int, input().split())
# graph = [[] for _ in range(v+1)]
visit = [False] * (v+1)
graph = [[]]

for _ in range(v):
    graph.append(list(map(int, input().split())))

print(graph)

def DFS(v):
    visit[v] = True
    print(v, end=' ')

    for i in graph[v]:
        if not visit[i]:
            DFS(i)

DFS(8)