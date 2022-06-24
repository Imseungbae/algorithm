# N x N 행렬
key = [
    [0,0,0],
    [1,0,0],
    [0,1,1]
]
    
# M X M 행렬
lock = [
    [1,1,1],
    [1,1,0],
    [1,0,1]
]

# 3배 확장 자물쇠 생성하기
def create_new_lock(lock):
    length =  len(lock)
    new_lock = [[0 for _ in range(length * 3)] for _ in range(length * 3)]

    for i in range(0, length):
        for j in range(0, length):
            new_lock[length + i][length + j] = lock[i][j]

    return new_lock

# key 시계방향으로 회전시키기
def rotate_key(key):
    row = len(key)
    col = len(key[0])
    new_key = [[0 for _ in range(col)] for _ in range(row)]

    for i in range(row):
        for j in range(col):
            new_key[j][i] = key[row - 1 - i][j]
    return new_key

# 2차원 배열 출력
def print_double_arr(arr):
    for i in arr:
        print(i)

# 자물쇠 체크
def check_lock(new_lock, lock):
    length = len(lock)
    
    for i in range(length, length * 2):
        for j in range(length, length * 2):
            if new_lock[i][j] != 1:
                return False
    return True

# 메인 솔루션 함수
def solution():
    global key
    new_lock = create_new_lock(lock)

    for i in range(len(lock) * 2 + 1):
        for j in range(len(lock) * 2 + 1):
            for _ in range(4):
                key = rotate_key(key)

                for i2 in range(0, len(key)):
                    for j2 in range(0, len(key)):
                        new_lock[i + i2][j + j2] += key[i2][j2]

                if(check_lock(new_lock, lock)):
                    print_double_arr(new_lock)
                    print("==================================")
                    return True

                for i2 in range(0, len(key)):
                    for j2 in range(0, len(key)):
                        new_lock[i + i2][j + j2] -= key[i2][j2]

    return False

# print( solution() )

n, m = 3, 5
test_arr = [[0] * n ]*m
test_arr_2 = [[0] * n for _ in range(m)]

print(test_arr)
print(test_arr_2)