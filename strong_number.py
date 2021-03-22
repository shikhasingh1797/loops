num=int(input('enter n num=')) 
a=num
sum=0
while num>0:
    i=1 
    fac=1
    rem=num%10
    while i<=rem:
        fac=fac*i
        i=i+1
    sum=sum+fac
    num=num//10
if sum==a:
     print('it is strong no')  
else:
     print('it is not strong no')        
