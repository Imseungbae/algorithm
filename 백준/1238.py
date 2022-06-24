# 20220419 화 1회 정답
import heapq, sys
input = sys.stdin.readline

v,e,n = map(int, input().split())
INF = int(1e9)

distance = [INF] * (v+1)
distance2 = [INF] * (v+1)
graph = [[] for _ in range(v+1)]
graph2 = [[] for _ in range(v+1)]

for i in range(e):
    a,b,c = map(int, input().split())
    graph[a].append((b,c))
    graph2[b].append((a,c))

def dijckstr(start, distance, graph):
    q = []
    distance[start] = 0
    heapq.heappush(q, (0, start))

    while q:
        dist, now = heapq.heappop(q)

        if distance[now] < dist:
            continue

        for i in graph[now]:
            cost = dist + i[1]
            dest = i[0]

            if distance[dest] > cost:
                distance[dest] = cost
                heapq.heappush(q, (cost, dest))

dijckstr(n, distance, graph2)
dijckstr(n, distance2, graph)

result = []
for i in range(1, len(distance)):
    result.append(distance[i] + distance2[i])

print(max(result))
