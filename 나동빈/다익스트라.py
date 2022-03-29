'''
다익스트라 : 최단경로 알고리즘
우선순위 큐를 이용한다
그리디 알고리즘으로 분류할 수 있다.

[input]
6 11
2
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
'''
import heapq

n, m = map(int, input().split())
INF = int(1e9)

start = int(input())

graph = [[] for _ in range(n+1)]
distance = [INF] * (n+1)

for _ in range(m):
    a,b,c = map(int, input().split())
    graph[a].append((b,c))

def dijkstra(start):
    q = []
    distance[start] = 0
    heapq.heappush(q, (0, start))

    while q:
        now = heapq.heappop(q)
        print(now[1], " 방문!!")

        if distance[now[1]] < now[0]:
            continue

        for i in graph[now[1]]:
            dist = i[1]
            dest = i[0]

            if distance[dest] > dist:
                distance[dest] = dist
                heapq.heappush(q, (dist, dest))

dijkstra(start)
for i in range(len(distance)):
    print(start, " 에서 ", i, " 까지 가는 최단거리는 ", distance[i])
