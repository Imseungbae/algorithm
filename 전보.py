# 노드의 갯수가 30,000 이므로 프로이드워셜말고 다익스트라 알고리즘을 선택
# 플로이드워셜 O(N^3) VS 다익스트라 O(ElogV)

import sys
import heapq
INF = int(1e9)
input = sys.stdin.readline

v, e, x = map(int, input().split())
dist = [INF] * (v+1)
graph = [[] for i in range(v+1)]

for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

def solution(start):
    q = [] # 우선순위 큐
    heapq.heappush(q, (0, start))
    dist[start] = 0

    while q:
        priority, now = heapq.heappop(q)
        # 현재노드가 이미 처리된 적이 있는 노드라면 무시
        if priority > dist[now]:
            continue
        for i in graph[now]:
            cost = priority + i[1]
            if dist[i[0]] > cost:
                dist[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

solution(x)
# 방문한 도시갯수
city_cnt = 0
for i in range(1, len(dist)):
    if dist[i] != INF:
        city_cnt += 1

# 방문하는데 걸린시간
time = max(dist[1:]) 

# cnt:시작노드제외 -1
print(city_cnt-1, time)