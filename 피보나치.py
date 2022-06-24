# dfs 구현
v, e = map(int, input().split())
graph = [[0] for _ in range(v+1) ]
visit = [False] * (v+1)

for i in range(1, v+1):
    graph[i] =  list(map(int, input().split()))

def DFS(n):
    visit[n] = True
    print(n, end=' ')
    for i in graph[n]:
        if not visit[i]:
            DFS(i)

DFS(1)

'''
입력값
8 9
2 3 8
1 7
1 4 5
3 5
3 4
7
2 6 8
1 7
'''

# 출력값
# 1 2 7 6 8 3 4 5 