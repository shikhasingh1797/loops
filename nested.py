num=int(input("enter a num="))
square=0
while num>0:
    r=num%10
    square=r*r
    dipu=square
    num=num//10
    print(dipu,end=" ")