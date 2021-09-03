# 위상정렬 구현하기
from collections import deque

# 노드와 간선 입력받기
v, e = map(int, input().split())

# 진입차수 리스트 선언
indegree = [0] * (v+1)

# 그래프 입력받기
graph = [ [] for i in range(v+1)]
for _ in range(e):
    a,b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1
# print( graph[1:] )
# print( indegree[1:] )

# deque선언
q = deque()
for i in range(1, v+1):
    if indegree[i] == 0:
        q.append(i)

#위상정렬 솔루션
def solution():
    while q:
        # q 가장 왼쪽값 pop
        now = q.popleft()
        print ( now )
        # now노드에 연결된 간선 제거
        for i in graph[now]:
            indegree[i] -= 1

            if indegree[i] == 0:
                q.append(i)

solution()