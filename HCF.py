a=int(input("enter any number="))
b=int(input("enter any number="))
while a%b!=0:
    rem=a%b
    a= b
    b=rem
print("HCF is = ",b)                                                                                                                                                          