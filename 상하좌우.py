# n = int(input())
# x = 1
# y = 1

# def check(x,y):
#     global n
#     if x < 1 or x > n:
#         return False
#     if y <1 or y > n:
#         return False
#     return True

# def rotate(dir):
#     global x
#     global y

#     if dir == "L" and check(x, y-1):
#         y -= 1
#     if dir == "R" and check(x, y+1):
#         y += 1
#     if dir == "U" and check(x, x-1):
#         x -= 1
#     if dir == "D" and check(x, x+1):
#         x += 1

# dir = list(input().split())

# for i in dir:
#     rotate(i)

# print(x, y)

############## 책 풀이 #############
n = int(input())
x, y = 1, 1
plans = input().split()

#L R U D
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_types = ['L', 'R', 'U', 'D']

for plan in plans:
    for i in range(len(move_types)):
        print("local_1", locals())
        if plan == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]
        if True:
            print("local_2", locals())
    if nx < 1 or nx > n or ny < 1 or ny > n:
        continue
    x, y = nx, ny
print(x, y)

