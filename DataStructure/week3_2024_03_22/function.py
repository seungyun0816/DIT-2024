"""
함수 사용

"""
def sayHello(name):
    print('안녕하세요 %s씨!'%(name))

'''
매개변수의 순서를 모르는 경우, 직접 
'''
def intro(myName,age):
    print('저는 {}세, {}입니다.'.format(age,myName))


'''
매개변수의 크기를 미리 알 수 없는 경우(값을 받기 전 까지 모르는 경우)
*을 사용하면 list형식으로 변환하여 전달

'''

def fruits(*fruits):
    for i in fruits:
        print(i)

'''
함수는 만들 때 기본 값 설정 가능
함수가 호출 될 때 매개변수가 없으면, 기본 값으로 매개변수를 사용
원하는 매개변수만 넣고, 나머지는 기본 값으로 사용 가능
'''

def intro(myName = '권상근',age = 21):
    print('저는 {}세, {}입니다.'.format(age,myName))

'''
예시로,
myName은 기본 값을 사용하고,age는 매개변수를 직접 지정

intro(age=55)
저는 55세, 권상근입니다.
'''

def div(a,b):
    q = a // b
    r = a % b
    return q,r







