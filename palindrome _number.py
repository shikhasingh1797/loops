num=int(input("enter any numbewr="))
rev=0
x=num
while num>0:
    rev=(rev*10)+num%10
    num=num//10
if x==rev:
    print("it is a palindrome number")
else:
    print("it is not a palindrome number")


    
    