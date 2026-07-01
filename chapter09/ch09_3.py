class Unit :
    def __init__(self, name, hp, speed):
        self.name = name
        self.hp = hp
        self.speed = speed

    def move(self, location) :
        print(f'{self.name} 유닛이 {location}방향으로 가고 있습니다.')


# 공격력이 있는 유낫(상속)
class AttackUnit(Unit): 

     # 생성자
    def __init__(self, name, hp, speed, damage):
        # 다중상속때 문제가 발생하니 super 사용 금지
        # super().init(name, hp, speed)
        # 부모를 책임짐
        Unit.__init__(self, name, hp, speed)
        self.damage = damage

  # 멤버함수
    def attack(self, location):
        print(f"{self.flying_speed} : {location} 방향으로 적군을 공격 합니다. [공격력 {self.damage}]")

    def damaged(self, damage):
        print(f"{self.name} : {damage} 데미지를 입었습니다.")
        self.hp -= damage
        if self.hp <= 0:
            print(f"{self.name}은 파괴 되었습니다.")
        else:
            print(f"{self.name} 유닛은 체력이 {self.hp}가 남아있습니다.")


# 공중 유무 유닛 (공중에서 업무 진행할 수 있는지 체크)
class Flyable:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed

# 멤버함수
    def fly(self,name, location):
        print(f"{name}이 {self.flying_speed}으로 {location}시 방향으로 날아가고 있습니다.")

# 다중상속 (지상공격유닛, 공중유무 유닛)
# AttackUnit(name, hp, speed, damage), Flyable(flying_speed):
class FlyableAttackUnit(AttackUnit, Flyable):
    def __init__(self, name, hp, speed, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, speed, damage)
        Flyable.__init__(self, flying_speed)

    # 오버라이딩
    def move(self, location) :
        print(f'{self.name} 공중 유닛이 {location} 방향으로 가고 있습니다.')

# 공격 기능 - intercepter 객체 생성
intercepter = FlyableAttackUnit('요격기1', 300, 0, 80, 200)
intercepter.attack('14시')
intercepter.damaged(60)
intercepter.fly(intercepter.name, '14시')
intercepter.move('15시')