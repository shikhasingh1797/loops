i=2
a=0
b=0
c=0
while i<=100:
    s=2
    count=0
    while s<i:
        if i%s==0:
            count=count+1
        s=s+1
    if count==0:
        if i%2==0:
            print(i,"even prime number")
            a=a+1
        else:
            print(i,"odd prime number")
            b=b+1
    else:
        print(i,"not prime number")
        c=c+1
    i=i+1
print(a,"total even prime number")
print(b,"total odd prime number")
print(c,"total not prime number")

