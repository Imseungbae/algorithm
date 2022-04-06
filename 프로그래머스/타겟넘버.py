import sys
from collections import deque

input = sys.stdin.readline

arr = list(map(int, input().split()))
target = int(input())

def bfs_solution():
    answer = 0

    q = deque()
    q.append((arr[0], 0))
    q.append((-1 * arr[0], 0))

    while q:
        temp, idx = q.popleft()
        idx += 1

        if idx < len(arr):
            q.append((temp + arr[idx], idx))
            q.append((temp - arr[idx], idx))
        else :
            print('temp: ' , temp)
            if target == temp:
                answer += 1
    return answer

answer = 0
def dfs_recur_solution(temp, idx):
    global answer
    if idx == len(arr):
        if target == temp:
            answer += 1
        return 
    dfs_recur_solution(temp + arr[idx], idx+1)
    dfs_recur_solution(temp - arr[idx], idx+1)

# dfs_recur_solution(arr[0], 0)

def dfs_stk_solution(start):
    answer = 0
    q = []

    q.append((arr[start], start))
    q.append((-1*arr[start], start))

    while q:
        temp, idx = q.pop()
        idx += 1

        if idx < len(arr):
            q.append((temp + arr[idx], idx))
            q.append((temp - arr[idx], idx))
        else :
            if target == temp:
                answer += 1
    
    return answer

print( dfs_stk_solution(0) )


'''
입력
4 1 2 1
0  
출력
2

그래프문제로 치환하는게 포인트
그래프문제로 치환 후 DFS/BFS로 완전탐색을 해결하면 된다.
세가지 풀이법이 있다.
BFS, DFS스택, DFS재귀 끝
'''