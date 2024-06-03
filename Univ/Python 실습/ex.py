'''
a = int(input('첫 번쨰 정수를 입력하세요. :'))
b = int(input('두 번쨰 정수를 입력하세요. :'))
c = int(input('세 번쨰 정수를 입력하세요. :'))
print('평균겂은 :',(a+b+c)/3)
'''
'''
def multi(a,b):
    return a*b
x = int(input('x = '))
y = int(input('y = '))
print('x x y =',multi(x,y))
'''
'''
def max(a,b,c):
    if a>=b and a>=c:
        return a
    elif b>=a and b>=c:
        return b
    else:
        return c
    
x, y, z = input('세 정수 입력: ').split()
x = float(x)
y = float(y)
z = float(z)

mx = max(x,y,z)
print('최대 값:',mx)
'''
'''
n=0
def Deci(a,b,c):
    return b ** 2 - 4 * a * c

a, b, c = input('세 실수 입력').split()
a = float(a)
b = float(b)
c = float(c)
deci = Deci(a,b,c)
'''
'''
def cube(width,deep,height):
    if height == 0:
        return width*deep*1
    else:   
        return width*deep*height

a = int(input('가로:'))
b = int(input('세로:'))
c = int(input('높이:'))

print('부피는:',cube(a,b,c))
'''
def varMax(*tp):
    mx = tp[0]
    for n in tp:
        if n > mx:
            mx = n
        
    return mx