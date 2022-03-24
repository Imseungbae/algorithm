n, m = map(int, input().split())
root = [0] * (n+1)

for i in range(1, n+1):
    root[i] = i

def findParent(node):
    if root[node] == node:
        return node
    else :
        return findParent(root[node])

def union(nodeA, nodeB):
    rootA = findParent(nodeA)
    rootB = findParent(nodeB)
    if rootA < rootB:
        root[rootB] = root[rootA]
    elif rootA > rootB :
        root[rootA] = root[rootB]
    else:
        print("cycle occur")
for _ in range(m):
    a, b = map(int, input().split())
    union(a,b)


for i in range(1, n+1):
    print(findParent(i))

print(root)




