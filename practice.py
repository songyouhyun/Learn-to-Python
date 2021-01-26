cabinet = {3:"유재석", 100:"김태호"}
print(cabinet.get(5, "사용가능"))           #5번째에 있는 거를 가져오려다가 5번에 아무것도 없으면 그다음 value값을 가져옴
print(3 in cabinet)

cabinet = {"13번 신발장":"유재석", "72번 신발장":"조세호"}
print(cabinet.get("13번 신발장"))       #결과값 : 유재석
print(cabinet.get("50번 신발장"))       #결과값 : none

#새 손님
print(cabinet)              #결과값 : {'A-20': '유재석', 'B-50':'조세호'}
cabinet["13번 신발장"] = "김종국"      #원래 있던 유재석이 김종국으로 바뀜
cabinet["54번 신발장"] = "박명수"     #박명수가 "C-100"에 추가
print(cabinet)              #결과값 : {'A-20': '김종국', 'B-50': '조세호', 'C-100': '박명수'}

#빠진 손님
del cabinet["13번 신발장"]         #김종국이 삭제됨
print(cabinet)              #결과값 : {'B-50': '조세호', 'C-100': '박명수'}

#지금 총 사용중인 고객 목록
#key 값들만 출력
print(cabinet.keys())       #결과값 : dict_keys(['B-50', 'C-100'])

#value 값들만 출력
print(cabinet.values())

#key값과 value값 둘다 출력
print(cabinet.items())

#목욕탕 폐점
cabinet.clear()
print(cabinet)