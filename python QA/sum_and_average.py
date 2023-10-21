'''write a program to take a tuple of numbers from the keyboard and print its sum and average'''
t=eval(input("enter tuple of numbers"))
sum=0
l=len(t)
for i in t:
    sum=sum+i
print("the sum=",sum) 
print("the average=",sum/l)   
