# 전역변수 지역변수

car_total = 100

def rent(rent_count) :
    # 지역변수
    car_total = 200
    if car_total > rent_count :
        car_total = car_total - rent_count
        print('렌트할 차 {}대 가능합니다. (가능 대여 차 개수 : {})'.format(rent_count,car_total))
    else :
        print('차가 없어 불가능합니다.')

rent(20)
print(car_total)