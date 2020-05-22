a=[int(x) for x in input().split(' ')]
num1=a[0]
num2=a[1]
while True:
    if(num1==0):
        print(num2)
        break
    if(num2==0):
        print(num1)
        break
    if(num1>num2):
        num1=num1%num2
    elif(num2>num1):
        num2=num2%num1
    else:
        print(num1)
        break
                  