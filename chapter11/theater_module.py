# 모듈

# 일반성인 입장료
def price(count) :
    price = 14000
    print(f'일반성인\n{count}명 영화 가격 : {count*price}(1인당 : {price})')

# 조조할인(40%) 
def price_morning(count) :
    price = int(14000 * 0.6)
    print(f'조조할인\n{count}명 영화 가격 : {count*price}(1인당 : {price})')

# 군인할인(60%)
def price_military(count) :
    price = int(14000 * 0.4)
    print(f'군인할인\n{count}명 영화 가격 : {count*price}(1인당 : {price})')





