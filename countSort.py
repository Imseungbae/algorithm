#카운트소트 구현 2021-08-10
arr = [7,5,9,0,3,1,6,2,9,1,4,8,0,5,2]

cntArr = [0] * (max(arr) + 1)
for i in arr:
    cntArr[i] += 1

for i in range(len(cntArr)):
    for j in range(cntArr[i]):
        print(i,end = ' ')
