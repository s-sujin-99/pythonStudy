# 파일입출려
'''
# 파일 -> w : 저장, r : 읽기, a : 추가
file_handle = open('score.txt','w', encoding='utf8')
print('국어 : 90', file=file_handle)
print('수학 : 92', file=file_handle)
print('엉어 : 100', file=file_handle)
file_handle.close()

# 추가 기능
file_handle = open('score.txt','a', encoding='utf8')
print('자바 : 90', file=file_handle)
print('파이썬 : 92', file=file_handle)
file_handle.close()

# 추가 기능 - write() 기능은 /n 기능이없다
file_handle = open('score.txt','a', encoding='utf8')
file_handle.write('html : 100\n')
file_handle.write('css : 90\n')
file_handle.close()

# 파일 읽어오기 read() 모두 읽어옴
file_handle = open('score.txt','r', encoding='utf8')
print(file_handle.read())
file_handle.close()

# 한줄씩만 읽기 readline()
file_handle = open('score.txt','r', encoding='utf8')
print(file_handle.readline(), end='')
print(file_handle.readline(), end='')
print(file_handle.readline(), end='')
print(file_handle.readline(), end='')
print(file_handle.readline(), end='')
print(file_handle.readline(), end='')
print(file_handle.readline(), end='')
print(file_handle.readline(), end='')
file_handle.close()

file_handle = open('score.txt','r', encoding='utf8')
exitFlag = False
while not exitFlag :
    # EOF이면 line = False
    line = file_handle.readline()
    print(line, end='')
    if not line :
        exitFlag = True
   
file_handle.close()

# list로 읽기
file_handle = open('score.txt','r', encoding='utf8')
list = file_handle.readlines()

for data in list :
    print(data, end='')
file_handle.close()
'''



