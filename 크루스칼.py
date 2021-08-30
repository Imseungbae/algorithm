# 크루스칼 알고리즘 구현
import sys
import heapq

input = sys.stdin.readline

v, e = map(int, input().split())

graph = [ [] for i in range(v+1)]

parent = [0] * (v+1)

cost = 0

for i in range(1, v+1):
    parent[i] = i

def find_parent(parent, n):
    if n != parent[n]:
        parent[n] = find_parent(parent, parent[n])
    return parent[n]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b

q =[]
for _ in range(e):
    a,b,c = map(int, input().split())
    heapq.heappush(q, (c,a,b))


while q:
    c, a, b = heapq.heappop(q)
    if find_parent(parent, a) == find_parent(parent, b):
        print("사이클 발생")
        continue
    else :
        union_parent(parent, a, b)
        cost += c

print( cost )
