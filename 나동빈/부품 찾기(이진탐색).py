import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
arr.sort()
m = int(input())
targetArr = list(map(int, input().split()))

def binarySearch(target):
    str = 0
    end = len(arr) - 1

    while str <= end:
        mid = (str+end)//2

        if target == arr[mid]:
            return 'yes'
        elif target < arr[mid]:
            end = mid - 1
        else : 
            str = mid + 1
    
    return 'no'


for i in targetArr:
    print( binarySearch(i) )

'''
5
8 3 7 9 2
3
5 7 9
no
'''