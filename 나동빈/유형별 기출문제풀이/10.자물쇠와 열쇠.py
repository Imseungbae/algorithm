# 자물쇠와 키 입력 받기
key = [[0,0,0], [1,0,0], [0,1,1]]
n = len(key)
lock = [[1,1,1], [1,1,0], [1,0,1]]
m = len(lock)

# 자물쇠 크기조정 배열 초기화
arr = [ [0 for _ in range(m*3)] for _ in range(m*3)]

# 자물쇠 그리기
for i in range(m, m+m):
    for j in range(m, m+m):
        arr[i][j] = lock[i-3][j-3]

# 자물쇠 체크
def check_lock():
    result = True

    for i in range(m, m+m):
        for j in range(m, m+m):
            if arr[i][j] != 1:
                result = False
    return result

# 열쇠 세팅
def set_key(x, y, key):
    n = 0 # 행
    m = 0 # 열

    for i in range(x, x + len(key)):
        # print("here : ", y + len(key))
        for j in range(y, y + len(key)):
            # print("i,j : ", i, j)
            # print("n,m : ", n, m)
            arr[i][j] += key[n][m]
            m += 1

        m = 0
        n += 1

    print(x,y, "로 이동")

    if check_lock():
        return True

    n = 0 # 행
    m = 0 # 열
    for i in range(x, x + len(key)):
        # print("here : ", y + len(key))
        for j in range(y, y + len(key)):
            # print("i,j : ", i, j)
            # print("n,m : ", n, m)
            arr[i][j] -= key[n][m]
            m += 1

        m = 0
        n += 1

    return False

# 시계방향 회전
def rotate_a_matrix_by_90_degree(before):
    n = len(before)     # 행 계산
    m = len(before[0])  # 열 계산
    after = [ [0 for _ in range(m)] for _ in range(n)] # 회전결과

    for i in range(n):
        for j in range(m):
            after[i][j] = before[n-1-j][i]

    return after

# 메인함수
for i in range(m*2+1):
    result = False
    
    for j in range(m*2+1):
        print("==============[", i, j, "]===============")
        
        for k in range(4):
            print("==[", k, "]==")
            result = set_key(j, i, key)
            key = rotate_a_matrix_by_90_degree(key)
            print("체크:: ", result)

        if result:
            break

    if result:
        break