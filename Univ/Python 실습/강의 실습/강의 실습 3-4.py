# def fibo(n) :
#     if n == 1 or n == 2 :
#         return 1
#     return fibo(n-1)+fibo(n-2)
    
# for n in range(1, 13) :
#     print(fibo(n), end=', ')
# print()

# a, b = 1, 1
# for n in range(1000) :
#     c = a + b
#     print(c, end=' ')
#     a = b
#     b = c

import random
for n in range (100):
    di = random.randint(1, 9)
    print(di, end=' ')