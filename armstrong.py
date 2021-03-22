num=int(input("enter the num--"))
a=num
sum=0
count=len(str(num))
while a>0:
    rem=a%10
    sum=sum+rem**count
    a=a//10
if sum==num:
    print("it is a armstorng numbrer")
else:
    print("it is not a armstrong number")
    