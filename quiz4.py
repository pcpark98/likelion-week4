def add(num1,num2):
    print("{0} + {1} = {2}".format(num1,num2,num1+num2))

def sub(num1,num2):
    print("{0} - {1} = {2}".format(num1,num2,num1-num2))

def mul(num1,num2):
    print("{0} * {1} = {2}".format(num1,num2,num1*num2))

def div(num1,num2):
    print("{0} / {1} = {2}".format(num1,num2,num1/num2))

while(True):
    operation=input("원하는 숫자를 입력하세요 1. 더하기 2. 빼기 3. 곱하기 4. 나누기 5. 종료")

    if(operation=="5"):
        print("종료합니다.")
        break
    else:
        num1=int(input("숫자 1을 입력하세요 : "))
        num2=int(input("숫자 2를 입력하세요 : "))
        if(operation=="1"):
            add(num1,num2)
        elif(operation=="2"):
            sub(num1,num2)
        elif(operation=="3"):
            mul(num1,num2)
        elif(operation=="4"):
            div(num1,num2)
