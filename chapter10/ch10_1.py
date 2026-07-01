# 예외처리

'''
# 두수를 입력받아 나눗셈하는 결과값 출력하는 프로그램
while(True) :
    try:
        num1 = int(input('숫자를 입력해주세요 :'))
        num2 = int(input('숫자를 입력해주세요 :'))
        print('{} / {} = {:.2f}'.format(num1,num2, num1/num2))
        break   
    except ValueError :
        print('오류가 발생')
    # except ZeroDivisionError as e:
    #     print(f'0은 안됩니다. 다시 입력해주세요\n{e}')
    except Exception as e :
        print(e)
    finally:
        print('finally')
print('프로그램 종료')
'''

'''
# 오류를 사용자가 조건에 따라서 발생
while(True) :
    try:
        num1 = int(input('숫자를 입력해주세요 :'))
        num2 = int(input('숫자를 입력해주세요 :'))
        # 조건 - 두수는 0보다 크고 10보다 작거나 같다
        if 0 < num1 <=10 and 0 < num2 <= 10 :
            print('{} / {} = {:.2f}'.format(num1,num2, num1/num2))
        else :
            raise ValueError
        break   
    except ValueError :
        print('오류가 발생')
    # except ZeroDivisionError as e:
    #     print(f'0은 안됩니다. 다시 입력해주세요\n{e}')
    except Exception as e :
        print(e)
    finally:
        print('finally')
print('프로그램 종료')
'''
'''
# 던더 메소드 생성후 실행
class SpecialClass():
    def __init__(self):
        print('생성자 생성')
    # toString
    def __str__(self):
        return '내가 만들고 싶은 문자열 생성후 전송'

sc = SpecialClass()
print(sc)
'''

# 사용자가 정의한 예외처리
class MyException(Exception):
    def __init__(self, message):
        self.message = message
    
    def __str__(self):
        return '{}예외 발생'.format(self.message)

# 사용자가 정의한 예외처리로 진행
while(True) :
    try:
        num1 = int(input('숫자(1-10)를 입력해주세요 :'))
        num2 = int(input('숫자(1-10)를 입력해주세요 :'))
        # 조건 - 두수는 0보다 크고 10보다 작거나 같다
        if 0 < num1 <=10 and 0 < num2 <= 10 :
            print('{} / {} = {:.2f}'.format(num1,num2, num1/num2))
        else :
            raise MyException('조건이 맞지 않습니다. ({},{}) '.format(num1,num2))
        break   
    except ValueError :
        print('오류가 발생')
    except MyException as e:
        print(f'사용자가 정의한 예외 발생\n{e}')
    except ZeroDivisionError as e:
        print(f'0은 안됩니다. 다시 입력해주세요\n{e}')
   

print('프로그램 종료')




