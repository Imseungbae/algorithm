## 나의 풀이 ##
import sys
input = sys.stdin.readline
INF = int(1e9)

v,e = map(int,input().split())
graph = [ [] for i in range(v+1) ]

for _ in range(e):
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

x, k = map(int, input().split())

# start->end 최단경로 리턴
def solution(start, end):
    dist = [INF] * (v+1)
    dist[start] = 0
    q = []
    q.append(start)
    while q:
        now = q.pop()
        for i in range(len(graph[now])):
            # i[0] 목적지노드
            cost = dist[now] + 1
            if cost < dist[graph[now][i]]:
                dist[graph[now][i]] = cost
                q.append(graph[now][i])
    return dist[end]

result = solution(1, k) + solution(k, 4)

if result == INF:
    print(-1)
else :
    print(result)


## 동빈님의 풀이##