a=int(input("enter any number="))
b=int(input("enter any number="))
i=1
if a<b:
    min=a
else:
    min=b
while(1):
    if i%a==0 and i%b==0:
        print("LCM = ",i)
        break
    i=i+1
