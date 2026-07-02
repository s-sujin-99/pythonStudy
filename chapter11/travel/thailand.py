# 클래스 모듈 생성

class ThailandModule:
    # 디폴트 생성자 
    # 멤버 함수
    def detail_travel(self):
        print('태국 여행 4박 5일 패키지 (방콕, 야시장투어, 해변투어, 잠수투어) 가격 : 60만원')

 
#  잘되는지 테스트
if __name__ == '__main__': 
    print('ThailandModule 위치입니다.')
    test_obj = ThailandModule()
    test_obj.detail_travel()
else :   # 외부에서 모듈 사용
    print('외부에서 호출 후 사용중입니다.')