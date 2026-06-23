#문자열 : 주석으로 여백, 공백, 기능까지 모두포함해서 문자열 취급
'''
message = '파이썬을 공부하고 있습니다.'
print(message, type(message))
message1 = """
파이썬을 
공부하고
있습니다.
"""
print(message1, type(message1))
'''

#슬라이싱 : 원하는 만큼 데이터 자르기
'''
id = '990229-4234567'
bth = id[:6]
gender = id[7]
userGender =''
if gender == '1' or gender == '3':
    userGender = '남자'
elif gender == '2'or gender == '4' :
    userGender = '여자'

print(f'사용자 생년월일은 {bth}이고 성별은 {userGender}입니다.')
'''

# 문자열 처리함수
'''
message = 'Python is Amazing'
# 소문자로 변환
print(message.lower())                  #python is amazing
# 대문자로 변환
print(message.upper())                  #PYTHON IS AMAZING
# 소문자만있는지 확인
print(message.islower())                #False
# 대문자만있는지 확인
print(message.isupper())                #False
# 문자열 바꾸기
print(message.replace('Python','Jave')) #Java is Amazing

# index보다 find를 사용 추천
# 적은 문자열 인덱스 반환 - 없으면 오류
print(message.index('is'))              #7
# 적은 문자열 인덱스 반환 - 없으면 -1반환
print(message.find('a'))                #12

# 적은 문자열 나온 횟수
print(message.count('n'))               #2
'''

# 문자열 포매팅
# %
'''
print('%s는 내가 좋아하는 과일입니다.' %('시과'))
print('PI는 %f입니다.' %(3.14))
print('내 나이는 %d입니다.' %(20))
'''

'''
# format
name = '홍길동'
age = 20
ment = '밥을 먹습니다.'

print('{}는 나이가 {}이고 지금 {}'.format(name, age, ment))
'''

# 탈출문자 

# \n: 줄 바꿈
print('안녕하세요.\n홍길동입니다.')
# \"와 \': 따옴표를 사용
print('안녕하세요.\'홍길동\'입니다.')
# \\: 역슬래시(\)를 사용
print('안녕하세요.\\홍길동\\입니다.')
# \r: 커서를 맨 앞으로 이동
print('안녕하세요.\r홍길동입니다.')
# \b: 앞 글자 하나를 삭제
print('안녕하세요.\b홍길동입니다.')
# \t: Tab 키와 같이 여러 칸을 띄울 때
print('안녕하세요.\t홍길동입니다.')



