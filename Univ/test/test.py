def Deci(a,b,c):
    d = b ** 2 - 4 * a * c
    if d > 0 :
      cnt = 2
    elif d == 0 :
        cnt = 1
    else :
        cnt = 0
    return cnt 

a, b, c = input('세 실수 입력 :').split()
a = float(a)
b = float(b)
c = float(c)
print('실근의 개수는', Deci(a,b,c))
