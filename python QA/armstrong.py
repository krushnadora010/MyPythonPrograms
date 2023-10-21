no=int(input("enter your number: "))
org=no
sum=0
while(no>0):
    sum=sum+(no%10)*(no%10)*(no%10)
    no=no//10
if(org==sum):
    print("this is a armstrong number")
else:
    print("this is not armstrong number")
            