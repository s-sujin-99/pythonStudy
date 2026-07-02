# 외장 함수
'''
# glob === window dir 기능
import glob

print(glob.glob('chapter11/*.py'))
'''
'''
# os : 운영체제 관련된 정보 확인
import os

# print(os.getcwd())

# 현재 dir에서 삭제 생성 진행
if os.path.exists('sample.txt') :
    print("파일이 존재합니다.")
    os.rmdir('sample.txt')
else :
    print('현재 파일을 찾을수 없습니다')
    answer = input('파일을 만들까요?')
    if answer == '네' :
        os.mkdir('sample.txt')
    else:
        print('파일을 만들지 않고 끝냅니다.')

# 현재 작업하는 폴더안에 리스트 보기
print(os.listdir())
'''

# 외장 함수 시간(time)
import time
print(time.localtime())
print(time.strftime('%Y-%m-%d %H:%M:%S'))

# 외장 함수 datetime
import datetime
print('오늘의 날짜는 :',datetime.date.today())

# 현재 날짜에서 100일 지난 날짜
today = datetime.date.today()
td = datetime.timedelta(days=100)
print(today + td)



