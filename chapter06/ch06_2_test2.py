'''
Quiz) 구구단 출력 프로그램을 만들어보자. 프로그램 사용자로부터 출력할 단
을 입력 받고, 해당 구구단을 출력하는 프로그램이다.
(for문과 while문 두가지 방식으로 구현해보자)
입력
몇 단을 출력할까요?: 5
'''
dan = int(input('몇단을 출력할까요? : '))


for j in range(1,10) :
    print('{} * {} = {}'.format(dan, j, dan*j))

print('')

exitFlag = False
count = 0
while not exitFlag :
    
    if  count > 8 :
        exitFlag = True
    else :
        count += 1
        print('{} * {} = {}'.format(dan, count, dan*count))



