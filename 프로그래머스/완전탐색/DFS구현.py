'''
[[[[[[[[[[입력값]]]]]]]]]
8 9
2 3 8
1 7
1 4 5
3 5
3 4
7
2 6 8
1 7
[[[[[[[[[출력값]]]]]]]]]
1 2 7 6 8 3 4 5 
'''
import sys
input = sys.stdin.readline
node, edge = map(int, input().split())

visit = [False] * (node+1)
graph = [[]]
result = []

for _ in range(node):
    graph.append(list(map(int, input().split())))

def dfs(node):
    visit[node] = True
    result.append(node)
    for i in graph[node]:
        if not visit[i]:
            dfs(i)

dfs(1)
print(result)