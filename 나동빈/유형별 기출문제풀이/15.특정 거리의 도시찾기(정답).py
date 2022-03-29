from collections import deque
import sys
input = sys.stdin.readline

n, m, k, x = map(int, input().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a,b = map(int, input().split())
    graph[a].append(b)

distance = [-1] * (n+1)
distance[x] = 0

def BFS():
    q = deque([x])

    while q:
        now = q.popleft()

        for i in graph[now]:
            if distance[i] < 0:
                distance[i] = distance[now] + 1
                q.append(i)
BFS()

for i in range(len(distance)):
    if distance[i] == k:
        print('노드 : ', i)

'''
4 4 2 1
1 2
1 3
2 3
2 4

4 4 1 1
1 2
1 3
2 3
2 4
'''