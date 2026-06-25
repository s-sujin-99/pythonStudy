# 반복문

list = [1,2,3,5,7,9]
for no in list :
    print('{}'.format(no), end=' ')
print('')

for no in [1,2,3,5,7,9] :
    print('{}'.format(no), end=' ')
print('')

for no in range(10,0,-1):
    print('{}'.format(no), end=' ')
print('')
    
orders =['햄버거','짜장면','짬뽕']
for data in orders :
    print('{}'.format(data), end= " ")
print('')

# 한줄 for문 - list comprehension
students = [1,2,3,4,5]
students = [ no + 10 for no in students ]
print(students)

students = [ no* 10 for no in students ]
print(students)

orders_len =[ len(data) for data in orders ]
print(orders_len)

like_subjects = ['java','python','html','javascript','Spring boot']
print(like_subjects)
upper_subjects = [ data.upper() for data in like_subjects ]
print(upper_subjects)

# 무한 반복문
count = 0
exitFlag = False
while not exitFlag :
    count += 1
    print('count : {}\n'.format(count), end=" ")
    if(count > 20) :
        exitFlag = True

# 변수 in [list 구조]
data = [1,2,3,4,5]
no = int(input("[1,2,3,4,5] 선택해주세요 : "))

# for i in data :
#     if no == 1 :
#         print("있어요.")
#         break
#     else :
#         print('없어요.')
       
if no in data :
    print('있어요')
else :
    print('없어요')