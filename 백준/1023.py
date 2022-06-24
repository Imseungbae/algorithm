'''
문제풀이 전략
괄호로 만들 수 있는 모든 문자열 경우의수 배열을 만든다.
그 중 괄호문자열을 제외시킨다.
제외시킨 배열에서 k번째 인덱스를 구한다.

n == 3
(((
(()
()(
())
)((
)()
))(
)))

))((
()()
(())

'''
from itertools import product

def sol(arr):
    lcnt = 0

    for i in range(len(arr)):
        if arr[i] == '(':
            lcnt += 1
        elif arr[i] == ')' :
            lcnt -= 1
            if lcnt < 0:
                return False
        if i == len(arr)-1:
            if lcnt == 0:
                return True
    return False

items = ['(', ')']

n, k = map(int, (input().split()))
arr = list(product(items, repeat=n))

result = []
for i in arr:
    if not sol(i):
        result.append(i)
if len(result) <= k:
    print(-1)
    quit()

result.sort()
for i in result[k]:
    print(i, end="")
print()