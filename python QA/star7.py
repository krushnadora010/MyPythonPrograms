no=int(input("enter the number of rows"))
i=1
while(i<no):
    b=1
    while(b<=i):
        print(" ",end=" ")
        b=b+1
    j=1    
    while(j<=i):
        print("*",end=" ")
        j=j+1   
    print()
    i=i+1
