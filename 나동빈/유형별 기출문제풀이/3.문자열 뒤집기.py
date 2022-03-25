str = input()
# zero = 0
# one = 0
# pre = ''

# for i in range(len(str)):
#     if pre == str[i]:
            # pre = str[i]
#         continue
#     if str[i] == '0' :
#         zero += 1
#     elif str[i] == '1' :
#         one += 1
#     pre = str[i]

# print( min(zero, one) )


# 번외 001001111 -> 0101로 변환하는 함수

def convert(str):
    pre = 'init'
    result = []
    for i in range(len(str)):
        if pre == str[i]:
            pre = str[i]
            continue
        result.append(str[i])
        pre = str[i]
    return result

print( convert(str) )
