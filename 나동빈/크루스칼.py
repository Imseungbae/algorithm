# 크루스칼 알고리즘은 최소신장트리를 구하는 알고리즘이다.
n, m = map(int, input().split())
graph = []
# 루트노드 리스트
parent = [0] * (n+1)

for i in range(1, len(parent)):
    parent[i] = i

for _ in range(m):
    a,b,c = map(int, input().split())
    graph.append((a,b,c))

def find_parent(a):
    if parent[a] != a:
        parent[a] = find_parent(parent[a])
    return parent[a]

def union(a, b):
    aa = find_parent(a)
    bb = find_parent(b)

    if aa < bb:
        parent[bb] = aa
    elif aa > bb:
        parent[aa] = bb
    else :
        return False
    return True

# 간선거리를 기준으로 오름차순 정렬 O(nlogn)
graph.sort(key=lambda x:(x[2]))
result = 0
for i in graph:
    if union(i[0], i[1]):
        result += i[2]

print(graph)
print(result)

'''
7 9
1 2 29
1 5 75
2 3 35
2 6 34
3 4 7
4 6 23
4 7 13
5 6 53
6 7 25
'''