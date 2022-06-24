result = []

def solution(gold, n, m):
    for j in range(1,m):
        comp = []
        for i in range(n):    
            comp.append(gold[i][j-1])
            if i != 0:
                comp.append(gold[i-1][j-1])
            if i != n-1:
                comp.append(gold[i+1][j-1])

            gold[i][j] += max(comp)
    # 2차원배열 원소 중에서 최대값 얻기
    max_val = 0
    for i in gold:
        for j in i:
            max_val = max(max_val, j)
    result.append(max_val)

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))

    # dp 배열 생성
    dp = []
    index = 0
    for i in range(n):
        dp.append(arr[index:index+m])
        index+=m

    print("dp테이블 : ", dp)

    # 메인함수 실행
    solution(dp, n,m)

for i in result:
    print(i)

'''
2
3 4
1 3 3 2 2 1 4 1 0 6 4 7
4 4
1 3 1 5 2 2 4 1 5 0 2 3 0 6 1 2
'''