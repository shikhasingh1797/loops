apple=int(input("enter apple tree position="))
home=int(input("enter home position  -="))
fall_apple=int(input("total quantity of fallen apple="))
count=0
i=0
a=0
b=0
while fall_apple>0:
    fall=int(input("fall_apple="))
    a=apple+fall
    print(a)
    if a==home:
        count=count+1
    fall_apple=fall_apple-1
print("total fallen apple in home = ",count)