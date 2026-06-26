# 함수

# 선언
def open_func():
    print('드디어 함수 시작')

open_func()

# 매개변수
def add_num(num1, num2) :
    print('두수의 합은\n{} + {} = {}'.format(num1, num2, num1+num2))

add_num(3,4)

# 함수 기본값 설정 
def profile(name, age = 30, main_subject = 'java') :
    print('이름 : {}\n나이 : {}\n주 언어 : {}'.format(name, age, main_subject))

profile('홍길동', 24, 'python')
profile('박익명')

# 가변인자
def new_proflie(name, age, lang1, lang2, lang3) :
    print(name, age, lang1, lang2, lang3)

def new_proflie2(name, age, *language) :
    print(name, age)
    for lang in language :
        print('{}'.format(lang), end= " ")

new_proflie('홍길동', 24, 'c', 'java', 'python')
new_proflie2('홍길동', 24, 'c')

