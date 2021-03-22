num=int(input("enter any numbe="))
count=0
i=1
while i<=num:
    if num%i==0:
        count=count+1
    i=i+1
if count==2:
    print("it is a prime number")
else:
    print("it is not prime number")