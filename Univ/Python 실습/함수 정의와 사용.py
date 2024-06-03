# def accumulateSum(n):
#     sum = 0
#     for i in range(1, n+1):
#         sum += i
#     return sum

# n = int(input('자연수 입력: '))
# print(accumulateSum(n))

# def getGrade(score):
#     if score >= 90: grade = 'A'
#     elif score >= 80: grade = 'B'
#     elif score >= 70: grade = 'C'
#     elif score >= 60: grade = 'D'
#     else: grade = 'F'
    
#     return grade

# score = int(input('성적을 입력하세요: '))
# print(getGrade(score), '입니다.')

# def findMax(num1, num2):
#     max = num1
#     if max < num2:
#         max = num2
#     return max

# num1 = int(input('첫 번째 정수를 입력하세요: '))
# num2 = int(input('두 번째 정수를 입력하세요: '))

def exchange(a, b):
    temp = a
    print('a=', a, 'b=', b)
    a = b
    b = temp
    print('a=', a, 'b=', b)
    
a = input()
b = input()
print('a=', a, 'b=', b)
exchange(a, b)
print('a=', a, 'b=', b)