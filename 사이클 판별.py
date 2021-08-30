# 서로소 집합을 이용하여 그래프의 사이클판단
import sys
input = sys.stdin.readline

v,e = map(int, input().split())

parent = [0] * (v+1)

for i in range(1, v+1):
    parent[i] = i

def find_parent(parent, a):
    if parent[a] != a:
        parent[a] = find_parent(parent, parent[a])
    return parent[a]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a < b:
        parent[b] = a
    else :
        parent[a] = b

# 사이클발생여부 출력
isCycle = False

for _ in range(e):
    a, b = map(int, input().split())
    if find_parent(parent, a) ==  find_parent(parent, b):
        isCycle = True
        break
    else:
        union_parent(parent, a, b)

print("사이클 여부: ", isCycle)
