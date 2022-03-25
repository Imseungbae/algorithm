n = int(input())
arr = list(map(int, input().split()))

arr.sort()
group =[]
result = 0

for i in arr:
    group.append(i)
    members = len(group)

    if  members >= i:
        result += 1
        group = []

print( result )

'''
5
2 3 1 2 2

6
2 3 1 2 1 2

6
2 3 1 4 2 2
'''

# N = input()
# X = sorted(list(map(int, input().split())))
# total_group = 0
# group = 0

# for fear in X :
#     group += 1
#     if fear <= group :
#         total_group += 1
#         group = 0

# print(total_group)