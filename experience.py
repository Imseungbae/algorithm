array = [('바나나',2),('키위',5),('망고',1)]

def setting(data):
    return data[1]

# 튜플의 두번째값으로 정렬
result = sorted(array, key=setting, reverse=True)


# 람다이용
result = sorted(array, key=lambda x:x[1])
print(result)