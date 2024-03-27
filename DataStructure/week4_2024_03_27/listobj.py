"""
객체의 속성,메소드명 받아와서 넘버링하는 함수
showObject(obj):
    ....
    ....

a = []
showObject(a):

1:__add__
2:__class__
....
"""
a = [10,20,30,40,50]

def showObject(a):
    
    lst = dir(a)
    #lst에 속성,메소드명 list형으로 저장
    
    for i in lst:
        print(1 + lst.index(i),':',i,type(i))

showObject(a)
