import sys
input = sys.stdin.readline

# 노드, 간선 입력받기
v, e = map(int, input().split())
# 방문테이블
visit = [False] * (v+1)
# 그래프 입력받기
graph = [ [] for i in range(v+1)]

for i in range(1, v+1):
    graph[i] = list(map(int, input().split()))

print(graph[1:], visit[1:])

def dfs(graph, visit, now):
    visit[now] = True
    print("visit", now)

    for v in graph[now]:
        if not visit[v]:
            dfs(graph, visit, v)
start = 1
dfs(graph, visit, start)