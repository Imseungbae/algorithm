v,e = map(int, input().split())
parent = [0] * (v+1)

# 부모 테이블상에서, 부모를 자기 자신으로 초기화
for i in range(1, v+1):
    parent[i] = i

# 루트노드 찾기
def find_parent(parent, x):
    # 루트 노드가 아니라면, 루트 노드를 찾을 때까지 재귀적으로 호출
    if parent[x] != x:
        return find_parent(parent, parent[x]) 
    return x

# 두 원소가 속한 집합을 합치기
def union_parent(parent, a, b):
    parentA = find_parent(parent, a)
    parentB = find_parent(parent, b)

    if parentA < parentB:
        parent[parentB] = parentA
    else:
        parent[parentA] = parentB

# union 연산
for _ in range(e):
    a, b = map(int, input().split())
    union_parent(parent, a, b)

# 각 원소가 속한 집합출력
for i in parent:
    print( find_parent(parent, i+1) , end=" ")
print()
# 부모 테이블내용 출력
print(parent[1:])