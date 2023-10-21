# program to reverse internal content of each word
# input:Durga Software Solution
# output:agruD erawtfoS noituloS 

s=input("enter your string: ")
k=s.split()
k1=[]
i=0
while i<len(k):
    k1.append(k[i][::-1])
    i=i+1
print(k1)    
