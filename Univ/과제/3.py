num = []

while True : # 정수 입력 받기
    number = int(input("정수 입력 (-1 입력 시 종료): "))
    
    if number == -1 : # -1인 경우 프로그램 종료
        break
    
    num.append(number)

if num:  # 리스트가 비어있지 않은 경우에만 실행, 최댓값과 최솟값 출력
    print("가장 큰 수:", max(num))
    print("가장 작은 수:", min(num))
