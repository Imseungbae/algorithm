input_data = [
    [1,0,0,1],
    [1,1,1,1],
    [2,1,0,1],
    [2,2,1,1],
    [5,0,0,1],
    [5,1,0,1],
    [4,2,1,1],
    [3,2,1,1]
]
result = []

# 기둥 체크
def check_vertical(x,y,a,b):
    global result
    check = False

    print("x,y : ", x,y)
    print("result : ", result)

    # 바닥에 기둥설치하는 경우 참
    if y is 0:
        check = True
    else:
        for (x2,y2,b2) in result:
            # 보의 한쪽 끝부분 케이스 -> 현재 여기서 막힘[★★★★★★★★★★★★★★★★★]
            if (x2,y2,b2) == (x-1,y,1):
                if (x2,y2,b2) == (x,y,1):
                    check = False
                else :
                    check = True
            elif (x2,y2,b2) == (x,y,1):
                if (x2,y2,b2) == (x-1,y,1):
                    check = False
                else :
                    check = True
            print("보의 한쪽 끝부분 케이스 : ", check)

            # 또다른 기둥 케이스
            if (x2,y2) == (x,y-1):
                print("또다른 기둥 CASE")
                check = True
    if check:
        if b is 0:
            print("vertical delete : ", check)
            result.pop([x,y,a])
        else :
            print("vertical insert : ", check)
            result.append([x,y,a])

# 보 체크
def check_horizontal(x,y,a,b):
    global result
    result.append([x,y,1])

    if b is 0:
        print("horizontal delete")
    else :
        print("horizontal insert")



# ================ #
for i in input_data:
    x,y,a,b = i
    
    if a is 0:
        check_vertical(x,y,a,b)
    else :
        check_horizontal(x,y,a,b)

print(result)

