# 입출력


# 사용자로부터 입력 받기 -> 무조건 문자열
'''
mention = input('아이디를 입력하세요 : ')
print(mention)

num  = input('좋아하는 숫자를 입력하세요 : ')
print(num, type(num))

flag = input('여행을 좋아하시나요?(True/False) : ')
print(flag, type(flag))

gender = input('성별을 입력해주세요(M/F) : ')
print(gender, type(gender))
'''
# 원하는 타입으로 바꾸고 싶으면 형변환 시키기

#Qize 사용자 나이를 입력받아서 출력하는 프로그램
'''
age = int(input('나이를 입력해주세요 : '))
print(age)
print('당신의 나이는 {}살 입니다.'.format(age))
'''

# 출력관련 기능
'''
print('파이썬' + '자바') 
print('파이썬', '자바')
# 지정값으로 출력
print('파이썬', '자바', '자바스크립트', '스프링부트' ,sep=',')
# 줄바꿈 대신 지정값으로 출력
print('파이썬' + '자바', end='?') 
print('파이썬', '자바')
# 출력 대상 지정 (표준화면 출력, 표준에러 출력)
import sys 
print('파이썬', '자바', file=sys.stdout)
print('파이썬', '자바', file=sys.stderr)
'''
# 출력화면 서식 지정 
'''
scores = {
    '수학' : 100,
    '영어' : 90,
    '국어' : 70
}
# print(scores)

# 1. 공간 확보 정렬 ljust(size), rjsut(size) -> (자바 - %10s, %-10s) 
for key, valuse in scores.items() :
    print('key = {}, value = {}'.format(key, valuse))
    print(key.ljust(10), str(valuse).rjust(10), sep=',')

# 2. 미리 공간 확보하고 빈칸 0으로 채우기 : zfill(size) 
for i in range(1,21) :
    print("num : " +str(i).zfill(3))
'''


# 3. 원하는 형태의 출력포맷 지정
print('{}'.format(100))
print('{0}'.format(100))
print('{} {}'.format(100,200))
print('{0} {1}'.format(100,200)) # 번호가 인수의 순서를 결정
print('{1} {0}'.format(100,200))

print('{0: >10}'.format(100)) # 10칸을주고 빈공간 오른쪽으로 정렬
print('{0:_>10}'.format(100)) # 10칸을주고 언더바 오른쪽으로 정렬
print('{0:_>+10}'.format(100)) 
print('{0:_>-10}'.format(-100)) 

print('{0:,}'.format(100000000000000)) # 3자리씩 콤마
print('{0:+,}'.format(100000000000000)) # 양수 3자리씩 콤마
print('{0:-,}'.format(-100000000000000)) # 음수 3자리씩 콤마

print('{0:>+30,}'.format(100000000000000)) 
print('{0:_>+30,}'.format(100000000000000)) 

print('{0:f}'.format(3.141592))
print('{0:.1f}'.format(3.141592))
print('{0:10.1f}'.format(3.141592))



