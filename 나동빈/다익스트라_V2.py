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


import heapq, sys
input = sys.stdin.readline
INF = int(1e9)

v, e = map(int, input().split())
distance = [INF] * (v+1)
graph = [[] for _ in range(v+1)]

for _ in range(e):
    a,b,c = map(int, input().split())
    graph[a].append((b,c))

def dijkstra(start):
    distance[start] = 0
    q = []
    q.append((0, start))

    while q:
        dist, now = heapq.heappop(q)

        for i in graph[now]:
            if distance[now] < dist:
                continue
            dest = i[0]
            cost = dist + i[1]

            if distance[dest] > cost:
                distance[dest] = cost
                heapq.heappush(q, (cost, dest))

dijkstra(1)
print(graph, distance)
"""








'''
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
'''
import sys, heapq
input = sys.stdin.readline
INF = int(1e9)

# 노드와 간선 입력받기
n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]

# 그래프 입력받기
for _ in range(m):
    a,b,c = map(int, input().split())
    graph[a].append((b,c))

# 최단거리테이블
distance = [INF] * (n+1)

# 다익스트라 함수
def solution(start):
    q = []
    distance[start] = 0
    heapq.heappush(q, (0,start))

    while q:
        now = heapq.heappop(q)

        if distance[now[1]] < now[0]:
            continue

        for i in graph[now[1]]:
            cost = i[1] + now[0]
            dist = i[0]

            if distance[dist] > cost:
                distance[dist] = cost
                heapq.heappush(q, (cost, dist))

solution(1)
print(distance[1:])
