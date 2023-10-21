'''program to reverse order of words
input: learn python is very easy
output:easy very is python learn
'''
str=input("enter your string: ")
k=str.split()
k1=[]
i=len(k)-1
while i>0:
    k1.append(k[i])
    i=i-1
print(k1)    