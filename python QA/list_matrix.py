# in python we can represent matrix by using nested lists.
n=[[10,20,30],[40,50,60],[70,80,90]]
print(n)
print("elements by row wise:")
for i in n:
    print(i)
print("elements by matrix style:")
for i in range(len(n)):
    for j in range(len(n[i])):
        print(n[i][j],end=' ')
    print()            