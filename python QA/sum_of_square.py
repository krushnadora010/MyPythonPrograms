no=int(input("enter your number: "))
sum=0
while(no>0):
    sum=sum+(no%10)*(no%10)
    no=no//10
    
print("sum of square is",sum)
