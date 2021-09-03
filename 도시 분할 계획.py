# solution idea : 입력받은 그래프를 크루스칼 알고리즘을 통해 최소신장트리를 뽑아내고, 여기서 가장 코스트가 긴 간선을 제거하여
#                 마을을 분할한다.
import sys
import heapq

input = sys.stdin.readline

# v, e 입기받기
v, e = map(int, input().split())

# parent 리스트 선언
parent = [0] * (v+1)
for i in range(1, v+1):
    parent[i] = i

# 그래프 선언
graph = [ [] for i in range(v+1)]
q = []
# 간선과 비용 입력받기
for _ in range(e):
    a,b,c = map(int, input().split())
    graph[a].append((c,b))
    heapq.heappush(q, (c,a,b))

# find_parent
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

# union_parent
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a < b:
        parent[b] = a
    else :
        parent[a] = b

# 스패닝트리
def spanning_tree():
    result = 0
    maxV = []
    # 1. cost기준으로 정렬한다 => heapq로 해결
    # 2. 가장 적은 간선부터 꺼낸다
    while q:
        cost, a, b = heapq.heappop(q)
        
        # 2-1. 사이클이 아닌경우
        if find_parent(parent, a) != find_parent(parent, b):
            union_parent(parent, a, b)
            result += cost
            maxV.append(cost)
        else :
            continue
    return result - max(maxV)

print( spanning_tree() )