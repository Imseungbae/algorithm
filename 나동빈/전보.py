import sys, heapq
input = sys.stdin.readline
INF = int(1e9)

cityCnt = 0
totalTime = 0

n, m, start = map(int, input().split())
distance = [INF] * (n+1)
graph = [[] for i in range(n+1)]

for _ in range(m):
    a,b,c = map(int, input().split())
    graph[a].append((b,c))

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    global cityCnt

    while q:
        dist, now = heapq.heappop(q)

        if distance[now] < dist:
            continue

        for i in graph[now]:
            if distance[i[0]] > i[1] + dist:
                distance[i[0]] = i[1] + dist
                heapq.heappush(q, (i[1]+dist, i[0]))
                cityCnt += 1
                
dijkstra(start)
print(cityCnt, max(distance[1:]))