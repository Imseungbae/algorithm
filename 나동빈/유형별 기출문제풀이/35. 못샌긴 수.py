'''
내 풀이 => DP미사용..
'''
# ugly = []
# def isUgly(n):
#     while True:
#         if n%5 == 0:
#             n = n/5
#         elif n%3 == 0:
#             n = n/3
#         elif n%2 == 0:
#             n = n/2
#         elif n == 1 or n == 2 or n == 3 or n == 5:
#             return True
#         else :
#             return False

# for i in range(1, 1001):
#     if isUgly(i):
#         ugly.append(i)

# print(ugly[54])



# 교재 풀이
n = int(input())

# DP테이블 선언
ugly = [0] * n
ugly[0] = 1

# 2,3,5 인덱스
i2 = i3 = i5 = 0
# 2,3,5 곱한 값
next2, next3, next5 = 2, 3, 5

for l in range(1, n):
    ugly[l] = min(next2, next3, next5)

    if ugly[l] == next2:
        i2 += 1
        next2 = ugly[i2] * 2
    if ugly[l] == next3:
        i3 += 1
        next3 = ugly[i3] * 3
    if ugly[l] == next5:
        i5 += 1
        next5 = ugly[i5] * 5

print(ugly[n-1])