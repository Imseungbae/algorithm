'''
4 6
19 15 10 17
'''

n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort(reverse=True)

# 첫번째 방법 : O(2,000,000,000,000,000) => 시간복잡도가 매우 크므로 이방식으로는 풀 수 없다.
# for i in range(max(arr), 0, -1):
#     res = 0
#     for j in arr:
#         if j - i > 0:
#             res += j-i
#     if res >= m:
#         print(i)
#         break

# 두번째 방법 => 가능한 이진탐색을 활용 할 수 있도록 고민.
# 첫번째 방법은 최대높이에서 1씩 감소하며 찾는과정인데 여기서 1씩감소말고 이진탐색 활용
# O(NM) -> O(nlogm)
def binary(arr, str, end):
    if str>end:
        return -1

    mid = (str+end)//2

    res = 0 # 떡의 개수

    for i in arr:
        if i - mid > 0:
            res += i - mid

    print("mid : ", mid, " 떡의 길이 : ", res)

    if res > m:
        return binary(arr, mid+1, end)
    elif res < m:
        return binary(arr, str, mid-1)
    else :
        return mid
        
print( binary(arr, 0, max(arr)) )