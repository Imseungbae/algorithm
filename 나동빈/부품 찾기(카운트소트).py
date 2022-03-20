import sys
input = sys.stdin.readline

countArr = [0] * 1000001

n = int(input())
for i in input().split():
    countArr[int(i)] = 1
    
m = int(input())
targetArr = list(map(int, input().split()))

for i in targetArr:
    if countArr[i] == 1:
        print('Yes')
    else :
        print('No')

'''
5
8 3 7 9 2
3
5 7 9
'''