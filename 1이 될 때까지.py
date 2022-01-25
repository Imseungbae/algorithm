
n, k = map(int, input().split())

print(1/3, 1//3)

def sol_1() :
    global n, k
    result =0
    
    while(n > 1):
        if n%k==0 :
            n = n/k
            result += 1
        else :
            n -= 1
            result += 1
    return result


print(sol_1())