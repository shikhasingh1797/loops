i=2                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             
while i<10:
    s=2
    count=0
    while s<i:
        if i%s==0:
            count=count+1
        s=s+1
    if count==0:
        if i%2==0:
            print(i,"even prime number")
        else:
            print(i,"odd prime number")
    else:
        print(i,"not prime number")
    i=i+ 1