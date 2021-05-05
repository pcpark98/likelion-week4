class Person:
    def __init__(self,name):
        self.name=name

    def hello(self):
        print("안녕 내 이름은 {0}이야".format(self.name))

    def walk(self):
        print("나는 걷는 중")

class Worker(Person):
    def __init__(self, name, company):
        self.name=name
        self.company=company
        self.mental=50
    
    def hello(self):
        print("안녕 내 이름은 {0}이고 내가 다니는 회사는 {1}".format(self.name,self.company))
    
    def work(self):
        self.mental=self.mental-10
        if(self.mental>=0):
            print("나는 일하는 중, 내 멘탈지수 : {0}".format(self.mental))
        else:
            print("더는 일 못해")

worker=Worker("빌게이츠","삼성")
worker.hello()
worker.walk()
for i in range(7):
    worker.work()