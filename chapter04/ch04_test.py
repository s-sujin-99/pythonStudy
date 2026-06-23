'''
Quiz) 사이트별로 비밀번호를 만들어 주는 프로그램을 작성하시오
예) http://naver.com
규칙1 : http:// 부분은 제외 => naver.com 
규칙2 : 처음 만나는 점(.) 이후 부분은 제외 => naver 
규칙3 : 남은 글자 중 처음 세자리 + 글자 갯수 + 글자 내 'e' 갯수 + "!" 로 구성 (nav) (5) 
(1) (!)
예) 생성된 비밀번호 : nav51
'''

'''
# 웹사이트 이름 찾을 덱스 추출
webSite = 'http://naver.com'
findStartIndex = webSite.find('/')
startIndex = webSite.find('/', findStartIndex+1) +1
endIndex = webSite.find(".")

# 웹사이트 이름 추출
webName = webSite[startIndex :endIndex ]

# 규칙3
sliceWeb = webName[:3]
webNum = len(webName)
countE = webName.count('e')

# 비밀번호 만들기
newPw = sliceWeb + str(webNum) + str(countE) + '!'
print(f'생성된 비밀번호 : {newPw}')
'''

# 웹사이트 이름 추출
webSite = 'http://google.com'
webSiteName = webSite.replace("http://","")
findName = webSiteName.find('.')

webName = webSiteName[:findName]

# 규칙3
sliceWeb = webName[:3]
webNum = len(webName)
countE = webSiteName.count('e')

# 비밀번호 만들기
newPw = sliceWeb + str(webNum) + str(countE) + '!'
print(f'생성된 비밀번호 : {newPw}')