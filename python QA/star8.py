no=int(input("enter your number of rows : "))
i=1
while(i<=no):
    a=1  # print for only space
    while(a<=no-i):
        print(" ",end=" ")
        a=a+1
    j=1 # print for only #
    while(j<=i):
        print(i,end=" ")
        j=j+1
    print()        
    i=i+1        