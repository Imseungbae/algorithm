'''
시간제한 1초, 메모리 제한 128MB
5
R R R U D D
'''

n = int(input())
arr = input().split()
print(arr)
x = 1
y = 1
dx = [0,0,-1,1]
dy = [1,-1,0,0]
move_type = ['R', 'L', 'U', 'D']

def move(type):
    global x,y
    
    for i in range(len(move_type)):
        if type == move_type[i]:
            nx = x + dx[i]
            ny = y + dy[i]
    if nx < 1 or nx > n or ny < 1 or ny > n:
        return
    x,y = nx,ny
    
for i in arr:
    move(i)
    print(x,y)
