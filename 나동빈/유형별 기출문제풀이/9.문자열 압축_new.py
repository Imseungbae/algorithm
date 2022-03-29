'''
abcabcabcabcdededededede
xababcdcdababcdcd
aabbcc
'''

arr = 'aabbcc'
result = ''
for i in range(1, len(arr)//2 + 1):
    pre = arr[:i]
    count = 1

    for j in range(i, len(arr), i):
        now = arr[j:j+i]

        if now == pre:
            count += 1
        else :
            result += str(count) + pre if count > 1 else pre
            count = 1
        pre = now

    result += str(count) + pre if count > 1 else pre
    print(result)
    result = ''