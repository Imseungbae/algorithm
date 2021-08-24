# 경로압축을 통해 루트노드찾기 시간복잡도를 개선한 서로소집합 구현
v, e = map(int, input().split())
parent = [0] * (v+1)

# 최초는 자기자신을 루트노드로 갖는다.
for i in range(len(parent)):
    parent[i] = i

# 루트노드를 찾는다
def find_parent(parent, n):
    if parent[n] !=n:
        parent[n] = find_parent(parent, parent[n])
    return parent[n]
    
# 유니온
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b) 

    if a < b:
        parent[b] = a
    else :
        parent[a] = b

for i in range(e):
    a, b = map(int, input().split())
    union_parent(parent, a, b)

print(find_parent(parent, 3))
