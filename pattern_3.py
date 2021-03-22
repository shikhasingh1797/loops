coloumn=1
while coloumn<=5:
    row=1
    while row<=5:
        if coloumn==1:
            print(row,end=" ")
        if coloumn==2:
            print(11-row,end=" ")
        if coloumn==3:
            print (row+10,end=" ")
        if coloumn==4:
            print(21-row,end=" ")
        if coloumn==5:
            print(row+20,end=" ")
        row=row+1
    print()
    coloumn=coloumn+1