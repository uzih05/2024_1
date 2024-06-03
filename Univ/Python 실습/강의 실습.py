'''
for dan in range(1,9,3):                                         # dan을 2, 6애 대해 반복
    for n in range(1,10):                                        # n을 1에서 9까지 1씩 증가시키며 반복
        for i in range(0,3):                                     # i을 0에서 3까지 1씩 증가시키며 반복
            print(dan+i, 'X', n,'=', (dan + i) * n, end = '\t')  # 구구단 출력
        print()
    print()
    
---------------------------------------

for x in range(5,0,-1):
    for space in range(0,5-x):
        print(' ',end=' ')
    for y in range(1,x+1):
        print(y, end=' ')
    print()

---------------------------------------

sum = 0.0
count = 0
k=[7.5,10.7,11.0,23.4,15.6,22.1,22.5,16.2]
for x in k:
    sum = sum + x
    count = 1

if count>0 :
    print('평균=', sum/count)
    
---------------------------------------

n = 1
while n <=10:
    print(n,end=(' '))
    n+=1
    
---------------------------------------

sum = 0
n = 0

score = int(input('점수 입력: '))     #점수를 받아 scoredp 저장
while (score != -1):                #만약 score가 -1이 아니면 반복
    sum += score                    #sum에 score를 누적
    n += 1
    score = int(input('점수 입력: ')) #점수를 받아 score에 저장
    
if n == 0:
    print('입력된 점수가 없습니다.')
else:
    print('합계: ',sum)
    print('평균: ', sum/n)
    
---------------------------------------

while True:
    str = input('단어 입력: ')
    if str == '종료':
        break
        
---------------------------------------

import random as r                  #random을 r로 지정(?)

randNum = r.randint(1,100)
inData = int(input('자연수 입력: '))
tryNum = 1                          #시도 횟수
while (inData != randNum):
    if (inData > randNum):
        print("더 작은 수 입니다.")
    else:
        print("더 큰 수 입니다.")
    inData = int(input('자연수 입력: '))
    tryNum += 1
    
print(tryNum, '번 시도에 맞추었습니다.')

---------------------------------------

n = 0
while n <= 99 :
    n+= 1
    if n%2 == 0 :
        continue
    print(n, end='\n')
'''