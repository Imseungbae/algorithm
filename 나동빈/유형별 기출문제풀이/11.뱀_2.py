from collections import deque

# 보드테이블 크기 입력받기 N X N
n = int(input())

# 사과 입력 받기 
apple_cnt = int(input())
apple = []
for _ in range(apple_cnt):
    x, y = map(int, input().split())
    apple.append((x-1,y-1))

# 이동리스트 입력 받기
move_cnt = int(input())
move_list = deque()
for _ in range(move_cnt):
    x, y = input().split()
    move_list.append((int(x), y))

# 방향연산배열
direction = [
    (-1, 0),
    (0, 1),
    (1, 0),
    (0, -1) 
]

# 방향을 방향연산배열 인덱스로 컨버팅
def dir_to_idx(dir):
    if dir == 'U':
        return 0
    elif dir == 'R':
        return 1
    elif dir == 'D':
        return 2
    elif dir == 'L':
        return 3

# 뱀 입력 받기
snake = deque([(0, 0)])
dir = 'R'

# 회전
def rotate(dir_ifno):
    global dir
    if dir == 'U':
        if dir_ifno == 'L':
            dir = 'L'
        elif dir_ifno == 'D':
            dir = 'R'
    elif dir == 'R':
        if dir_ifno == 'L':
            dir = 'U'
        elif dir_ifno == 'D':
            dir = 'D'
    elif dir == 'D':
        if dir_ifno == 'L':
            dir = 'R'
        elif dir_ifno == 'D':
            dir = 'L'
    elif dir == 'L':
        if dir_ifno == 'L':
            dir = 'D'
        elif dir_ifno == 'D':
            dir = 'U'

# 이동
def move():
    x, y = snake[len(snake)-1] # 뱀의 머리 좌표
    idx = dir_to_idx(dir)

    dx = x + direction[idx][0]
    dy = y + direction[idx][1]

    print("이동위치 : ", dx, dy)
    # 배열 벗어나는지 체크
    if dx >= n or dy >= n or dx < 0 or dy < 0:
        print("범위 초과!!!!!!!!!")
        return False

    # 꼬리에 닿는지 체크
    if (dx, dy) in snake:
        print("머리가 꼬리에 닿았다!!!!!")
        return False

    snake.append((dx, dy))

    # 사과 체크
    if (dx, dy) in apple:
        print("eat apple")
    else :
        snake.popleft()
    return True

def solution():
    time = 0

    while True:
        time += 1
        print(time, " ===========", snake)
        
        if len(move_list) > 0:
            cur_move = move_list.popleft()

        if not move():
            return time

        if cur_move[0] == time:
            rotate(cur_move[1])
        else :
            move_list.appendleft(cur_move)

print(solution())



'''
6
3
3 4
2 5
5 3
3
3 D
15 L
17 D
=> 9

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
=> 21

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
=> 13
'''