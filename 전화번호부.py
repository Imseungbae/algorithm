def solution(phone_book):
    answer = True
    dic ={} #key,value형태의 딕셔너리이용
    for pNumber in phone_book:
        dic[pNumber] = 1 #key:폰번호 value:1
    for pNumber in phone_book: #각각 폰번호마다 검사
        temp=""
        for num in pNumber: #폰번호를 한글자로 쪼개서 반복문 "243"이면 "2" "4" "3"
            temp +=num #쪼갠 숫자를 반복문이 돌아갈 때마다 붙음  
            if temp in dic and temp!=pNumber: #딕셔녀리의 키로 존재하는지 검사
                answer = False
    return answer


print( solution(["119", "97674223", "1195524421"]) )