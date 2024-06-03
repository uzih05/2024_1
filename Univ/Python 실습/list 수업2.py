data = []
while data != -1:
    lst.append(data)
    data = int(input('정수 입력 :'))

total, len, avg = 0, 0, 0
for n in lst :
    total += n
    len += 1

if len > 0 :
    prin('합계: ', total, '평균: ', total/len)
