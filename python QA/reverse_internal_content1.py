s=input("enter your string: ")
k=s.split()
k1=[]
i=len(k)-1
while i>=0:
    k1.append(k[i][::-1])
    i=i-1
print(k1)    
