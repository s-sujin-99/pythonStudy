# 숫자자료형
'''
print(5)
print(-5)
print(3.141592)
print(-3.141592) 
'''

# 숫자 자료형 계산 (+, -, *, /, %, //) 
# 연산식 순서 (최고, 단항, 이항:산술,쉬프트,비교,논리(비트:일반), 삼항, 치환, 컴마)
'''
print(5+5)
print(2*8)
print(6/4)
print(6%4)
print(6//4) # 몫
print(4 * (5 / 3))
'''

#문자열 자료형
'''
print('여름과일' + '수박')          #문자열 + 문자열 -> 문자열
print('당신의 나이는?' + str(28))   #문자열 + 숫자형 -> 형변환 str()
print('&' * 10)                   #문자열 * 숫자형 -> 숫자만큼 복사
print('오렌지', '토마토')           #빈칸이  생김
#escape 문자 \n => new Line, \r => return, \t => tab 
print('오늘은 "정말로" 공부를 열심히 했다.')  #큰/작은따옴표 사용법
'''

#불 자료형
'''
print(5>3)
print(5<3)
print(True)
print(False)
print(not(10 > 5))
'''

#변수(변하는 값을 저장해서 다음에 사용할 수 있도록 활용)
#전역변수, 지역변수
'''
animal = '강아지'
name = '너굴맨'
age = 4
hobby = '산책'
print('당신이 좋아하는 동물은?')
print('내가 좋아하는 동물은 ' + animal + '입니다. 이름은 ' + name + '입니다.')
print('너굴맨의 나이는 '+ str(age) +'살입니다. '+ hobby +'을 좋아합니다.')
'''

# 숫자형 자료형
'''
print(int('54') + 24)             #문자열 + 숫자형 -> 형변환 int()
print(float('3.4') + 4.2)         #문자열 + 숫자형 -> 형변환 float()
print(int(3.4))                   #실수를 정수로 형변환 가능 (문자열은 불가능)
'''

#type 확인
'''
print(type(3))                    # <class 'int'>
print(type('3'))                  # <class 'str'>
print(type(3.5))                  # <class 'float'>
print(type(True))                 # <class 'bool'>
print(type('a'))                  # <class 'str'>
'''


