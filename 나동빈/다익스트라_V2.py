"""
[입력데이터]
6 11
1 2 2
1 3 5
1 4 1
2 3 3
2 4 2
3 2 3
3 6 5
4 3 3
4 5 1
5 3 1
5 6 2
[출력데이터]
0
2
3
1
2
4
"""

import heapq, sys
input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())
dist = [INF] * (n+1)
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a,b,c = map(int, input().split())
    graph[a].append((b,c))

print(graph)

def dijackstra(start):
    q = []
    heapq.heappush(q, (0, start))
    dist[start] = 0

    while q:
        nowDestCost = heapq.heappop(q)
        nowCost = nowDestCost[0]
        nowDest = nowDestCost[1]

        if(dist[nowDest] < nowCost):
            continue

        for i in graph[nowDest]:
            dest = i[0]
            cost = i[1]

            if dist[dest] > cost + nowCost:
                dist[dest] = cost + nowCost
                heapq.heappush(q, (cost + nowCost, dest))
dijackstra(1)
print(dist)