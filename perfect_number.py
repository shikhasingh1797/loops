num=int(input("enter any number="))
i=1
s=0
while i<num:
    if num%i==0:
        c=i
        s=s+c
    i=i+1
if num==s:
    print(num,"is perfect number")
else:
    print("is not perfect number")     