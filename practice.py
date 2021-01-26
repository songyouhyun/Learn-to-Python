#세트 (set) = 집합
# 중복 안됨, 순서가 없음
my_set = {1,2,3,3}
print(my_set)           #결과값 : {1,2,3}


java_dev = {"유재석","김태호","양세형"}
python_dev = set(["유재석","박명수"])   #set로 감싸주고 list를 정의, 값은 위와 동일

#교집합 (java와 python을 모두 할 수 있는 개발자)
print(java_dev&python_dev)                      #결과값 : {'유재석'}
print(java_dev.intersection(python_dev))        #결과값 :    ""

#합집합 (java를 할 수 있거나, python을 할 수 있는 개발자)
print(java_dev | python_dev)                    #결과값 : {'양세형', '박명수', '유재석', '김태호'}
print(java_dev.union(python_dev))               #결과값 : {'양세형', '박명수', '유재석', '김태호'}
                                                #하지만 결과값이 출력할때마다 다르게 나옴, 순서가 없기 때문

#차집합 (java는 할 줄 알지만, python은 할 줄 모르는 개발자)
print(java_dev - python_dev)                    #결과값 : {'양세형', '김태호'}
print(java_dev.difference(python_dev))          #결과값 : {'양세형', '김태호'}
#or (python은 할 줄 알지만, java는 할 줄 알지만, python은 할 줄 모르는 개발자)
print(python_dev - java_dev)                    #결과값 : {'박명수'}
print(python_dev.difference(java_dev))          #결과값 : {'박명수'}

#python개발자 추가
python_dev.add("김태호") 
print(python_dev)                               #결과값 : {'박명수', '김태호', '유재석'}

#java개발자 해고
java_dev.remove("김태호")
print(java_dev)                                 #결과값 : {'양세형', '유재석}



############결과값 수정############