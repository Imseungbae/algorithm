import sys
input = sys.stdin.readline
from collections import deque
INF = 1e9
n = int(input())
graph = [ [] for i in range(n+1)]
for i in range(1, n+1):
    graph[i] = list(map(int, input().split()))

start = 1
q = deque()
q.append(start)
visit = [False] * (n+1)
visit[start] = True

def bfs(graph, q):
    while q:
        now = deque.popleft(q)
        print( "now", now )
        for i in graph[now]:
            if not visit[i]:
                q.append(i)
                visit[i] = True

bfs(graph, q)
print( graph )