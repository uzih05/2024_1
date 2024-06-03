studList = []
for n in range(5) :
    id, name, score = input('학번 이름 성적 입력 : ').split()
    studList.append([id, name, int(score)])
    
for i in range(4, -1, -1): # i = 4, 3, 2, 1, 0 반복
    for j in range(0, i):
        if studList[j][2] < studList[j+1][2] :
            studList[j], studList[j+1] = studList[j + 1], studList[j]
print('정렬결과: ', studList)
