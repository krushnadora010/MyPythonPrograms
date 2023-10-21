'''the process of giving another reference variable to the existing list is called aliasing.'''

x=[10,20,30,40]
y=x
print(id(x))
print(id(y))

x=[10,20,30,40,50]
y=x
print(x)
y[1]=100
print(y)

x=[10,20,30,40]
y=x.copy()
y[2]=80
print(y)
