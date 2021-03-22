num=int(input("enter a num="))
rev=0
while num>0:
    rev=rev*10+(num%10)
    num=num//10
a=rev
while a>0:
    r=a%10
    square=r*r
    dipu=square
    a=a//10
    print(dipu,end="")