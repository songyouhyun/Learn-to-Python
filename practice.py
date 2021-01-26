#Tuple
menu = ("돈까스","치즈까스")
print(menu[0])
print(menu[1])
#menu.add("생선까스")        #결과값 : Error / 이유 : Tuple은 값을 추가할 수 없음


#일반적인 변수 출력방법
name = "김종국"
age = 20
hobby = "코딩"
print(name,age,hobby)       #결과값 : 김종국 20 코딩

#Tuple을 활용한 변수 출력방법
(name, age, hobby) = ("김종국",20,"코딩")   #서로 다른 변수에 서로 다른 값들을 순서대로 넣어줄 수 있음
print(name,age,hobby)                    #결과값 : 위와 동일