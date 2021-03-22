num=int(input("enter a number="))
sum=0
count=0
while num>0:
    a=int(input("num="))
    sum=sum+a
    num=num-1
a=sum
while a!=0:
    a=a//10
    count=count+1
b=sum/count
print(b)