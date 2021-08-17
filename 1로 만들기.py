d = [0] * 30001
def makeOne(X):
    if X==1:
        return 0
    value = makeOne(X-1) + 1 
    if X%3==0:
        return min(value, makeOne(X//3) + 1)
    if X%2==0:
        return min(value, makeOne(X//2)) + 1
    if X%5==0:
        return min(value,makeOne(X//5)+1)

N = int(input())
print(makeOne(N))