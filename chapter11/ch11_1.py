# 모듈 가져와서 사용
'''
# 별칭도 가능
import theater_module as tm

# 일반성인 
tm.price(3)

# 조조 할인
tm.price_morning(3)

# 군인 할인
tm.price_military(3)
'''

# 그냥 사용
# *에다가 함수 이름 넣으면 지정 사용 가능 (별칭)
# from theater_module import price as p
# p(3)

from theater_module import *
price(3)
price_morning(3)
price_military(3)


