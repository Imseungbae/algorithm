# topological_sort로 구현
from collections import deque
import copy
v = int(input())

graph = [ [] for _ in range(v+1)] 
indegree = [0] * (v+1)
time_list = [0] * (v+1)

# 값 입력받기
for i in range(1, v+1):
    # 강의시간 입력
    input_list = list(map(int, input().split())) # 1, 2, 1, -1
    time_list[i] = input_list[0]
    for j in input_list[1:-1]:
        graph[j].append(i)
        indegree[i] += 1

# print(graph[1:])

def topological_sort():
    q = deque()
    result_list = copy.deepcopy(time_list)
    # indegree 0인 값들 큐에 저장
    for i in range(1, len(indegree)):
        if indegree[i] == 0:
            q.append(i)
    # 큐가 빌때 까지 반복
    while q:
        now = q.popleft()
        for i in graph[now]:
            # i = 2,3,4 now = 1
            result_list[i] = max(result_list[i], result_list[now] + time_list[i])
            indegree[i] -= 1
            if indegree[i] == 0:
                q.append(i)
    print( result_list[1:] )
topological_sort()

# input
# 5
# 10 -1
# 10 1 -1
# 4 1 -1
# 4 3 1 -1
# 3 3 -1

