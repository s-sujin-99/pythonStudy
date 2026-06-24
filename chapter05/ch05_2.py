# 딕셔너리 key, value값
# key는 중복 X
'''
menu = {
    '커피' : 4000,
    '바나나우유' : 2000,
    '에너지 드링크' : 2500
}
print(menu)

# 값변경
menu['커피'] = 5000
print(menu)

# 값추가
menu['핫바'] = 2700
print(menu)

# 값삭제
del menu['바나나우유']
print(menu)

# 키값 존재 확인
print('핫바' in menu)
'''

# 값확인
'''
# key값 확인
print(menu.keys())

# value 확인
print(menu.values())

# 둘다 확인
print(menu.items())

# 딕셔너리에 있는 모든 값 삭제
menu.clear()
print(menu)
'''
