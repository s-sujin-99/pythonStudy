#연산자 - +, - , *, /, %, **, //
'''
print(3+2)
print(3-2)
print(3*2)
print(3/2)
print(3%2)
print(3**2)
print(3//2)
'''

#관계연산자 (<, >, <=, >=, ==, !=, and(&), or(|), 5 <= a <= 10)
'''
num = 5
print(2 < num < 10)             #True
print(not(2 < num < 10))        #False

print(num > 2 and num < 10)     #True
print(not(num >2 and num < 10)) #False
print(not(num >2 & num < 10))   #False
print(num < 2 or num > 10)      #False
print(num < 2 | num > 10)       #False
print(3>2)
print(3>=2)
print(3<2)
print(3<=2)
print(3==2)
print(3!=2)
'''
#수식 연산자
# print((5+4)* 2)

#복합대입연산자
'''
num = 10
num += 10                #num = num + 10
num -= 10                #num = num - 10
num *= 10                #num = num * 10
num /= 10                #num = num / 10
num **= 2                #num = num ** 10
num //= 10               #num = num // 10
num %= 2                 #num = num % 10
print(f'num : {num}')
'''

#함수
'''
num = 5
numList = [5,70,10,3,4]
print(abs(-num))             #절대값
print(pow(num,3))            #거듭제곱
print(max(numList))          #최댓값
print(min(numList))          #최솟값
print(round(3.141592,2))     #반올림값
'''

#모듈
'''
from math import *
num =3.141592
print(floor(num))
print(ceil(num))
print(sqrt(4))
'''

from random import *
'''
for i in range(0,10) :
    print(int((random()*(179 - 120 +1))+120))
'''
#randrange -> 마지막숫자 미포함
'''
for i in range(0,5) :
    print(randrange(1,101))
    print(int(random()*(125-120)+120))

'''
#randint -> 마지막숫자 포함
for i in range(0,5) :
    print(randint(1,100))
