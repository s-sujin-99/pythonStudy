# 외부 패키지를 다운로드 후 설치
# https://pypi.org/
# install 코드 복사후 terminal에 붙여넣기

from bs4 import BeautifulSoup
soup = BeautifulSoup("<p>Some<b>bad<i>HTML")
print(soup.prettify())

# 원하는 데이터 찾기
find_str = input('찾고싶은 데이터 : ')
print(soup.find(string="bad"))

if soup.find(string=find_str):
    print('원하는 데이터를 찾았어요')
else :
    print('원하는 데이터가 없어요')

# 원하는 태그 찾기
print(soup.p)