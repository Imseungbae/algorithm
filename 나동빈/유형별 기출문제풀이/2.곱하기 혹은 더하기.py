n = input()
sum = int(n[0])

for i in range(len(n)-1):

    if sum < 2 or int(n[i+1]) < 2:
        print(i, " +선택")
        sum += int(n[i+1])
    else :
        sum *= int(n[i+1])
        print(i, " *선택")
    
    print(sum)
