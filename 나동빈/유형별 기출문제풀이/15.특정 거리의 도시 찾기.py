# 전형적인 최단거리문제이므로 다익스트라나 플로이드워셜알고리즘이 떠오르지만 해법이 아니다.
# 모든 간선의 길이가 1이므로 BFS로도 최단거리를 구할 수 있다.

'''
4 4 2 1
1 2
1 3
2 3
2 4

5 5 2 1
1 2
1 3
2 3
2 4
2 5

4 3 2 1
1 2
1 3
1 4

4 4 1 1
1 2
1 3
2 3
2 4

'''

from collections import deque
import sys
input = sys.stdin.readline

n, m, k, x = map(int, input().split())
graph = [[] for _ in range(n+1)]
visit = [False] * (n+1)
step = 0
result = []

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

def BFS(graph, visit, start):
    q = deque()
    global step

    q.append((step, start))
    
    while q:
        step, v = q.popleft()
        if visit[v]:
            continue
        visit[v] = True

        if step == k:
            print('here : ', k)
            result.append(v)

        print('step : ', step, '방문 : ', v)

        for i in graph[v]:
            if not visit[i]:
                q.append((step+1, i))
                

BFS(graph, visit, x)
print(result)