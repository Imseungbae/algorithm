"""
[입력데이터]
6 11
1
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

import sys
import heapq

input = sys.stdin.readline
INF = int(1e9)

v,e = map(int, input().split())
start = int(input())

distance = [INF] * (v+1)
graph = [ []  for i in range(v+1) ]

for _ in range(e):
    a,b,c = map(int, input().split())
    graph[a].append((b,c))

def dijkstra(start):
    q =[]
    heapq.heappush(q, (0, start))

    # graph  0:노드 1:거리
    # heapq  0:거리 1:노드

    while q:
        dist, now = heapq.heappop(q)
        # 이미 방문한 노드는 pass처리
        if distance[now] < dist :
            continue            
        for graphItem in graph[now]:
            cost = graphItem[1] + dist
            if cost < distance[graphItem[0]]:
                distance[graphItem[0]] = cost        
                heapq.heappush( q, (cost, graphItem[0]))

        
dijkstra(start)

for i in range(1, len(distance)):
    if distance[i] == INF:
        print(0)
    else :
        print(distance[i])