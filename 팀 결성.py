import sys

input = sys.stdin.readline

v, e = map(int, input().split())
parent = [0] * (v+1)

for i in range(1, v+1):
    parent[i] = i

graph = [ [] * i for i in range(v+1)]

def find_parent(parent, n):
    if parent[n] != n:
        parent[n] = find_parent(parent, parent[n])
    return parent[n]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a < b:
        parent[b] = a
    else :
        parent[a] = b


for _ in range(e):
    a,b,c = map(int, input().split())
    graph[b].append(c)
    #합치기 연산
    if a == 0:
        union_parent(parent, b, c)
    #같은팀여부 확인 연산
    elif a == 1:
        if find_parent(parent, b) == find_parent(parent, c):
            print("YES")
        else:
            print("NO")