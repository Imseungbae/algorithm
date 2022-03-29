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
from collections import deque
import sys

input = sys.stdin.readline

v, e = map(int, input().split())
visit = [False] * (v+1)
graph = [[]]

for _ in range(v):
    graph.append(list(map(int, input().split())))

def BFS(graph, start, visit):
    q = deque()
    q.append(start)

    while q:
        now = q.popleft()

        if visit[now]:
           continue
         
        visit[now] = True
        print(now, end= ' ')

        for i in graph[now]:
            q.append(i)

BFS(graph, 1, visit)