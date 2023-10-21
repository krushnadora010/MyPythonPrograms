no=int(input("enter your number"))
x=no
rev=0
while(no>0):
    rev=rev*10+no%10
    no=no//10
if (x==rev):
    print("this is a palidrome number")
else:
    print("this is not palidrome number")        