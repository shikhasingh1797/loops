num=int(input("enter any number="))  
am=num
i=0
while am>0:
    z=am%10
    i=i+z
    am=am//10
if (num%i==0):
    print("it is a harsad number")
else:
    print("it is not a harsad number")                                          
    