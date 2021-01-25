#) 사이트별로 비밀번호를 만들어 주는 프로그램을 작성하시오

# EX) http://naver.com
# 규칙1 : http:// 부분은 제외 => naver.com
# 규칙2 : 처음 만나는 점(.) 이후 부분은 제외 => naver
# 규칙3 : 남은 글자 중 처음 세자리 + 글자 갯수 + 글자 내 'e' 갯수 + "!"로 구성

url = "http://naver.com"

pwd = url.replace("http://","")             #replace("원래 것","바뀔 것")
# print(pwd)                                #결과값 : naver.com

pwd = pwd[:pwd.index(".")]                  #처음부터 pwd의 .이 나오는 부분까지 슬라이싱
# print(pwd)                                #결과값 : naver

pwd = pwd[:3] + str(len(pwd)) + str(pwd.count("a")) + "!"
#pwd를 처음부터 3번째글자까지 슬라이싱 + str(글자 갯수) + str(글자 내 'e' 갯수)) + "!"  

print("{0}의 비밀번호는 {1} 입니다.".format(url,pwd))
