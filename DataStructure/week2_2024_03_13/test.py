Python 3.12.2 (tags/v3.12.2:6abddd9, Feb  6 2024, 21:26:36) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
print("Hello Python")
Hello Python
ds
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    ds
NameError: name 'ds' is not defined
txtHello = "Hello"
print(txtHello)
Hello
txtHello =
SyntaxError: invalid syntax
txtHello = null
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    txtHello = null
NameError: name 'null' is not defined
print(55%10)
5
print(53%11)
9
print(9**99)
29512665430652752148753480226197736314359272517043832886063884637676943433478020332709411004889
txtHello = 바보
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    txtHello = 바보
NameError: name '바보' is not defined
a,b = 200,300
print(a,' + ' b, ' = ', a+b)
SyntaxError: invalid syntax. Perhaps you forgot a comma?
print(a," + ", b, " = ", a+b)
200  +  300  =  500
a,b = 100,3.141592
print("a = %d, b = %f"%(a,b))
a = 100, b = 3.141592
print("a = %10d, b = %.3f"%(a,b))
a =        100, b = 3.142
print("a = %`0d, b = %2f"%(a,b))
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    print("a = %`0d, b = %2f"%(a,b))
ValueError: unsupported format character '`' (0x60) at index 5
print("a = %-10d, b = %.2f"%(a,b))
a = 100       , b = 3.14
print("a = %10d, b = %.3f"%(a,b))
a =        100, b = 3.142
print("a = {}, b = {}".format(a,b))
a = 100, b = 3.141592
print("a = {1}, b = {0}".format(a,b))
a = 3.141592, b = 100
print("a = {x}, b = {y}".format(x = a,y = b))
a = 100, b = 3.141592
print("DIT")
DIT
print("DIT")print("DIT")print("DIT")
SyntaxError: invalid syntax
print("DIT", end="!!)
      
SyntaxError: unterminated string literal (detected at line 1)
print("DIT", end"!!")
      
SyntaxError: invalid syntax
print("DIT", end="!!")
      
DIT!!
print("DIT", end="!!")
      
DIT!!
print(a," + ", b, " = ", a+b)
      
100  +  3.141592  =  103.141592
print(a,"+", b, "=", a+b)
      
100 + 3.141592 = 103.141592
print(a,"+", b, "=", a+b end="!END!")
      
SyntaxError: invalid syntax. Perhaps you forgot a comma?
print(a,"+", b, "=", a+b, end="!END!")
      
100 + 3.141592 = 103.141592!END!
print(a,"+", b, "=", a+b, sep="| |")
      
100| |+| |3.141592| |=| |103.141592
print(a,"+", b, "=", a+b, sep="")
      
100+3.141592=103.141592
print("Korean","Japan","China")
      
Korean Japan China
print("Korea","Japan","China" sep="")
      
SyntaxError: invalid syntax. Perhaps you forgot a comma?
print("Korea","Japan","China", sep="")
      
KoreaJapanChina
print("Korea","Japan","China", sep=",",end="!!!")
      
Korea,Japan,China!!!
name = input("당신의 이름은?")
      
당신의 이름은?승윤
print("안녕하세요, {}씨!".format(name))
      
안녕하세요, 승윤씨!
anyTxt = '%s'
      
print(anyTxt)
      
%s
print("출력란 : %S" %(anyTxt))
...       
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    print("출력란 : %S" %(anyTxt))
ValueError: unsupported format character 'S' (0x53) at index 7
>>> n = input("정수입력:")
...       
정수입력:100
>>> canTxt = txt
...       
Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    canTxt = txt
NameError: name 'txt' is not defined
>>> canTxt = "txt"
...       
>>> print("출력란 : %S" %(canTxt))
...       
Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    print("출력란 : %S" %(canTxt))
ValueError: unsupported format character 'S' (0x53) at index 7
>>> print("출력란 : %s" %(canTxt))
...       
출력란 : txt
>>> print("출력란 : %s" %(anyTxt))
...       
출력란 : %s
>>> print(int(n))
...       
100
>>> n = int(input("정수 입력:"))
...       
정수 입력:ㅁㅇㄴㅇㅁㄴ
Traceback (most recent call last):
  File "<pyshell#50>", line 1, in <module>
    n = int(input("정수 입력:"))
ValueError: invalid literal for int() with base 10: 'ㅁㅇㄴㅇㅁㄴ'
>>> 30
...       
30
>>> 32
...       
32
>>> n = int(input("정수 입력:"))
...       
정수 입력:45
>>> print(n+3)
...       
48
>>> n = input
...       
>>> 656
...       
656
>>> print(n)
...       
<built-in function input>
>>> n = input()
...       
dsadas
>>> print(n)
...       
dsadas
>>> )print("뒷 맛이 안 좋아", end="<<>>")
SyntaxError: unmatched ')'
>>> print("뒷 맛이 안 좋아", end="<<>>")
뒷 맛이 안 좋아<<>>
>>> print("중간 중간 찔리는게 있어", sep="W")
중간 중간 찔리는게 있어
>>> print("중간","중간","찔리는게","있어", sep="W")
중간W중간W찔리는게W있어
>>> print("내몫  = {1}, 니몫 = {0}".format(6000,4000))
내몫  = 4000, 니몫 = 6000
