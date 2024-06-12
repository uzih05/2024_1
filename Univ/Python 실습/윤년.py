year = int(input('년도 입력: '))
# year를 4로 나눈 나머지가 0이 아니라는 것을 의미
if year%4 != 0:
    print('%d년은 윤년이 아닙니다!'%year)
else:
    # year를 100으로 나눈 나머지가 0이라는 것을 의미
    if year%100 == 0:
        # yeaer를 400으로 나눈 나머지가 0이라는 것을 의미
        if year%400 == 0:
            print('%d년은 윤년입니다!'%year)
        # 400으로 나눴을 때 0이 아니라면,
        else:
            print('%d년은 윤년이 아닙니다!'%year)
    #100으로 나눴을 떄 0이 아니라면,
    else:
        print('%d년은 윤년입니다!'%year)
