result = []
flag = 0
progresses= [93,30,55]
speeds = [1,30,5]

while(True):
    flag += 1
    print("progressess=", progresses)
    for j in range(len(progresses)):
        progresses[j] += speeds[j]
    temp = 0
    while progresses[0] >= 100:
        progresses.pop(0)
        temp += 1
        result.append(temp)

    if flag == 15:
        break