from collections import deque

n = int(input())
_map = [[False for i in range(n+1)] for i in range(n+1)]

apple_cnt = int(input())

for i in range(apple_cnt):
    a,b = map(int, input().split())
    _map[a][b] = True

# 시작 지점
start = (1,1)

# 전역 변수
time = 0
head = start
snake = deque()
snake.append(start)

cur = 0
dir_type = ['R', 'D', 'L', 'U']
dx = [0,1,0,-1]
dy = [1,0,-1,0]

# 동작을 배열로 입력받는다
action_cnt = int( input() )
actions = deque()
for _ in range(action_cnt):
    x, c = input().split()
    actions.append((int(x), c))

# 방향 전환 함수
def rotate(dir):
    global cur
    print('rotate 실행 before: ', cur)
    if dir == 'L':
        cur = (cur - 1) % 4
    else :
        cur = (cur + 1) % 4
    print('rotate 실행 after:', cur)


# 이동 함수
def move():
    global snake, time, cur, head

    # 이동할 좌표
    nx = head[0] + dx[cur]
    ny = head[1] + dy[cur]

    # 게임 종료조건 체크 1.벽 충돌 2.자기자신 충돌
    if nx < 1 or ny < 1 or nx >n or ny > n:
        print("[벽과 충돌!!!!!!!!!!!] 게임 종료 시간 : ", time)
        return False

    for i in snake:
        if (nx, ny) == (i[0], i[1]):
            print("[자기 자신과 충돌!!!!!!!!!] 게임 종료 시간 : ", time)
            return False

    head = (nx, ny)
    
    # 사과를 처먹은 경우
    if _map[nx][ny]:
        print('사과를 먹은 경우')
        _map[nx][ny] = False
        snake.append(head)
    else :
        print('사과를 못먹은 경우')
        snake.append(head)
        snake.popleft() # == pop(0)

    return True

# 메인 함수
def solution():
    global time, head, snake

    # 리팩터링
    while True:
        time += 1
        if not move():
            break

        print("snake : ", snake)
        
        if actions:
            print("time : ", time)
            print("target_time : ", actions[0][0])
            if time == actions[0][0]:
                target_time, dir = actions.popleft()
                rotate(dir)
    print("종료시간 : ", time)

# 메인 함수 호출
solution()

'''
case 1================ 9
6
3
3 4
2 5
5 3
3
3 D
15 L
17 D

case 2================ 21
10
4
1 2
1 3
1 4
1 5
4
8 D
10 D
11 D
13 L

case 3================ 13
10
5
1 5
1 3
1 2
1 6
1 7
4
8 D
10 D
11 D
13 L
'''