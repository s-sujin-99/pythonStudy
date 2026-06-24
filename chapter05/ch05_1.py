# 자료구조
# list
'''
num = [10,20,30]
print(str(num))
# 추가 - 마지막 인덱스로
num.append(40)
print(str(num))
# 삽입 - 원하는 인덱스로
num.insert(1,50)
print(str(num))
# 삭제 - 마지막값 삭제
num.pop()
print(str(num))
'''

# list 함수
# count 중복값확인
'''
num = [10,10,20,30,40,50]
print(str(num.count(10)))

# 정렬
# sort() -> 오름차순 / sort(reverse=True) -> 내림차순
num.sort(reverse=True)
print(f'{num}')

# 원래 순서를 반대로
num.reverse()
print(f'{num}')

# 원본을 건들지 않고 정렬된 리스트 생성
newNum = sorted(num)
print(f'{newNum}')
'''

# 확장

num1 = [10,20,30]
num2 = [40,50,60]
num1.extend(num2)

print(f'{num1}')
print(num1+num2)

