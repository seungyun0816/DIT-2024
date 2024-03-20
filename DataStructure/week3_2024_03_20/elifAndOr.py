"""
1~10범위의 수를 입력하여 소수이면 '소수'
아니면 '소수 아님' 범위를 벗어나면 '잘못된 입력'출력하기
"""
n = int(input('1~10의 숫자 입력'))

if 11 > n > 0 :
    if n == 2:
        print('소수')
    elif n == 3:
        print('소수')
    elif n == 5:
        print('소수')
    elif n == 7:
        print('소수')
    else:
        print('소수아님')
else :
    print('잘못된 입력')
