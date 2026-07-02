# 내부에서 Package 가져오는 방법
# Package === 폴더(여러개 모듈을 포함)

# travel속에 thailand 모듈 
# import안에 해당되는 클래스나 함수는 가져오면 안됨
import travel.thailand as travel_t

thailand_obj = travel_t.ThailandModule()
thailand_obj.detail_travel()

# travel속에 vietnam 모듈 
# import안에 클래스나 함수 가져오는 방법
from travel.vietnam import VietnamModule

vietnam_obj = VietnamModule()
vietnam_obj.detail_travel()

'''
# 해당되는 패키지에 모든 모듈 가져오기
# __init__에서 __all__쓰면 가져올수 있음
from travel import *

t_obj = thailand.ThailandModule()
t_obj.detail_travel()

v_obj = vietnam.VietnamModule()
v_obj.detail_travel()
'''
'''
# 패키지 모듈 위치
import inspect 
import random
# inspect를 이용한 random패키지 위치 검사
print(inspect.getfile(random))

from travel import *
# inspect를 이용한 thailand패키지 위치 검사
print(inspect.getfile(thailand))
'''



