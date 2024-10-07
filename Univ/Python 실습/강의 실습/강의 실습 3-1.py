import math

def dist(x1, y1, x2, y2):
    return math.sqrt((x1-x2)**2 + (y1-y2)**2)
    
x1, y1 = 0, 0
x2 = float(input('x의 값: '))
y2 = float(input('y의 값: '))

r = dist(x1, y1, x2, y2)
print('거리는', r, '입니다.')
