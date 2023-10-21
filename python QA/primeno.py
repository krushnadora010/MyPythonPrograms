no=int(input("enter your number: "))
i=1
count=0
while(i<=no):
    if(no%i==0):
       count=count+1
    i=i+1

if(count==2):
    print("it is a prime number",)
else:
    print("t is a not prime number")  
