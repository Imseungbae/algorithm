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
import sys, heapq
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[]]
for _ in range(n):
    graph.append(list(map(int, input().split())))

visited = [False] * (n+1)

def bfs(start):
    q = []
    visited[start] = True
    q.append(start)

    while q:
        now = heapq.heappop(q)

        for node in graph[now]:
            if not visited[node]:
                heapq.heappush(q, node)
                visited[node] = True
                print(node, "방문")

start = 1
print(start, "방문")
bfs(start)