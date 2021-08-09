from collections import deque
n,m = map(int,input().split())
graph = []
dq = deque([(0, 0, 2)])
cnt = 0
for _ in range(n):
    graph.append(list(map(int,input().split())))

def bfs(cnt):
    while dq:
        (x,y,z) = dq.popleft()
        cnt = z
        if x<0 or x>=n or y<0 or y>=m:
            continue
        if graph[x][y] == 1:
            graph[x][y] = cnt
            dq.append( (x, y+1, cnt+1) ) #동
            dq.append( (x-1, y, cnt+1) ) #남
            dq.append( (x, y-1, cnt+1) ) #서
            dq.append( (x+1, y, cnt+1) )  #북
    

bfs(0)
print(graph[n-1][m-1] -1)