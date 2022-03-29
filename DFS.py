# DFS 구현하기

import sys
input = sys.stdin.readline

# 노드와 간선 입력받기
v, e = map(int, input().split())
# 방문리스트
visit = [False] * (v+1)
graph = [ [] for i in range(v+1)]
# 그래프 입력받기
for i in range(1, e):
    a = list(map(int, input().split()))
    graph[i] = a

# print( graph )

def dfs(graph, visit, node) :
    visit[node] = True
    print( node, end=' ' )
    for i in graph[node]:
        # 미방문
        if visit[i] == False:
            visit[i] = True
            dfs(graph, visit, i)
        # 방문
        else:
            pass
dfs(graph, visit, 1)


# 입력값
# 8 9
# 2 3 8
# 1 7
# 1 4 5
# 3 5
# 3 4
# 7
# 2 6 8
# 1 7

# 출력값
# 1 2 7 6 8 3 4 5 