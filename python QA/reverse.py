# write a program to reverse the given string
name=input("enter your name: ")
print(name[::-1])

n=input("enter your name: ")
print(''.join(reversed(n)))

name1=input("enter your name: ")
i=len(name1)-1
rev=""
while i>0:
    rev=rev+name1[i]
    i=i-1
print(rev)    


