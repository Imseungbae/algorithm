arr = input()
alpha = []
sum = 0

for i in arr:
    if i.isalpha():
        alpha.append(i)
    else :
        sum += int(i)

alpha.sort()
if sum >= 0:
    alpha.append(str(sum))

print(''.join(alpha))
'''
AJKDLSI412K4JSJ9D
'''
