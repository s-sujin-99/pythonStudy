'''
Quiz) 주어진 코드를 활용하여 부동산 프로그램을 작성하시오.
(출력 예제) 총 3대의 매물이 있습니다. 
강남 아파트 매매 10억 2010년 
마포 오피스텔 전세 5억 2007년 
송파 빌라 월세 500/50 2000년
'''
class House :
    # 매물 초기화
    def __init__(self, location, house_type, deal_type, price, completion_year) :
        self.location = location
        self.house_type = house_type
        self.deal_type = deal_type
        self.price = price
        self.completion_year = completion_year
    # 매물정보 표시
    def show_detail(self) :
        print(f'{self.location} {self.house_type} {self.deal_type} {self.price} {self.completion_year}년')

# 객체 생성
house1 = House('강남','아파트','매매','40억',2010)
house2 = House('마포','오피스텔','전세','5억',2007)
house3 = House('송파','빌라','월세','500/50',2000)

# 리스트 선언
house = []

# 값 추가
house.append(house1)
house.append(house2)
house.append(house3)

# 출력
print(f'총 {len(house)} 매물이 있습니다.')
# house1.show_detail()
# house2.show_detail()
# house3.show_detail()
for houses in house:
    houses.show_detail()
