# write a program to access each character of string in forword and backword direction by using  while loop ?

str=input("enter your string: ")
n=len(str)
i=0
print("forword direction")
while i<n:
    print(str[i],end="")
    i=i+1
print()
print("backword direction")
i=-1
while(i>=-n):
    print(str[i],end='')
    i=i-1    
