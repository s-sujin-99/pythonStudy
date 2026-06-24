'''
Quiz)게임에서 각 방에 숨겨진 아이템 개수를 나타내는 2차원 리스트가 있다. 모든 
방을 돌아다니며 아이템을 수집하는 프로그램을 작성하세요. 아이템이 없는 방은 0
으로 표시된다.
rooms = [ [3, 1, 2], [2, 0, 1], [1, 3, 2] ] 
힌트) sum(리스트)는 리스트의 합계를 계산해 준다.
for room in rooms:
total += sum(room)
실행결과
총 수집한 아이템 수 : 15

'''

rooms = [[3,1,2],[2,0,1],[1,3,2]]
total = 0
for room in rooms :
    total += sum(room)

print(f'총 수집한 아이템 수 : {total}')