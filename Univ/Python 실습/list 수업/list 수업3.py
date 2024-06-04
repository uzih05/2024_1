lst = []
for i in range(5):
    dat = float(input('%d번째 실수 : '%i))
    lst.append(dat)
sum(lst)
len(lst)
print('합계=', sum(lst), '평균', len(lst))
