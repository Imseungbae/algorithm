# https://www.acmicpc.net/problem/1316
# 그룹단어체커 - 문자열
answer = 0

n = int(input())
arr = []

for _ in range(n):
    arr.append(input())

# 리스트를 이용한 풀이
# 문자열의 문자들을 차례대로 집합에 추가한다.
# 현재문자가 집합에 존재하고, 이전문자와 같다면 -> 그룹단어가 아니다
# 이외의 케이스는 그룹단어이다.
def use_arr(answer):
    for string in arr:
        check_set = set(string[0])
        flag = True

        for i in range(1, len(string)):
            if string[i] in check_set and string[i-1] != string[i]:
                flag = False
            check_set.add(string[i])

        if flag:
            answer += 1
    return answer

#인덱스를 이용한 풀이
def use_index(answer):
    for string in arr:
        flag = True
        for i in range(len(string)-1):
            if string[i] == string[i+1]:
                pass
            else :
                new_string = string[i+1:]
                if string[i] in new_string:
                    flag = False
        if flag:
            answer += 1
    return answer

def solution(answer):
    # print(use_arr(answer))
    print(use_index(answer))

# 메인 실행
solution(answer)