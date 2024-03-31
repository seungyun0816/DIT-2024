class Person:

    def __init__(self, name):

        self.name = name

        self.아는사람 = []

        self.만난횟수 = {}

        self.tmt = False

    #--------------------------

    def 인사하기(self, you):

        if 0 != len(self.아는사람): #아는 사람이 1명 이상이면

            for i in self.아는사람: #아는 사람 숫자만큼 아는 사람 목록 하나씩 가져오기
                
                if you.name == i:   #매개변수로 받아 온 객체의 이름과 현재 가져온 아는 사람의 이름이 같으면

                    if 5 > self.만난횟수[i] >= 1: #1번 이상 만난 대상애게 하는 인사
                    
                        self.다시인사(you)

                    elif self.만난횟수[i] >= 5:
                        
                        self.친한사이(you)
                        
                        
            if you.name not in self.아는사람: #인사 할 대상이 아는 사람 목록에 없는 경우

                self.첫인사(you)
            
        else:   
            
            self.첫인사(you)
                
    #--------------------------

    def 첫인사(self, you):
        
        print("안녕하세요 {}씨, 저는 {}입니다.".format(you.name, self.name))

        self.기억하기(you.name)

        you.기억하기(self.name)

        if self.tmt:
            
            print("이제 {}는 아는 사람입니다.".format(you.name))

    #--------------------------                    

    def 기억하기(self, name):

        self.아는사람.append(name)

        self.만난횟수[name] = 1

    #--------------------------

    def 다시인사(self ,you):

        print("또 만나 반갑습니다 {}씨!!".format(you.name))

        self.만난횟수[you.name] += 1

        you.만난횟수[self.name] += 1

    #--------------------------

    def 친한사이(self, you):
        
        print('ㅎㅇ')

        self.만난횟수[you.name] += 1

        you.만난횟수[self.name] += 1

#--------------------

p1 = Person("홍길동")

p2 = Person("이순신")

p3 = Person("강감찬")

p2.tmt = True
