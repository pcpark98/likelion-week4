fruits=[]

for i in range(5):
    fruit=input("{0}번 과일을 입력하세요 : ".format(i+1))
    fruits.append(fruit)


for i in range(5):
    print("{0}번째 과일은 {1}입니다.".format(i+1,fruits[i]))