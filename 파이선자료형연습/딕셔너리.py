# # # # # # # # #
# # 딕셔너리 훈련 # # 
# # # # # # # # #

# 1. 선언
dictionary = {"key1" : "value1", "key2" : "value2"}
dictionary["key2"] = "value3"

dict2 = dict()
dict2[1] = "first"
dict2[2] = "second"
dict2[3] = "third"
dict2[4] = "four"
dict2[5] = "five"
dict2[6] = "six"

# 2. key 조회 O(1)
if 1 in dict2:
    print("yess")

# 3. value 조회 O(1)
if 'first' in dict2.values():
    print("yesser")

# 4. key 전부 조회
for key in dict2.keys():
    print(key)

# 5. value 전부 조회
for val in dict2.values():
    print(val)

# 6. items 하나씩 출력
for item in dict2.items():
    print(item[0], " 과 ", item[1])

# 7. get으로 null safty하게 조회
print("get함수를 써서 안전하게 get :", dict2.get(5))

# 8. 딕셔너리 아이템 삭제
del dict2[6]
print("get함수를 써서 안전하게 get :", dict2.get(6))

# 9. 딕셔너리 아이템 value로 삭제


# 10. 딕셔너리 모든 아이템 삭제
dict2.clear()
print(dict2)