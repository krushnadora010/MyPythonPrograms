str=input("entrer your string: ")
print("forword direction")
for i in str:
    print(i,end="")
print()    
print("forword direction")
for i in str[::]:
    print(i,end="")
print()    
print("backword direction")
for i in str[::-1]:
    print(i,end="")

