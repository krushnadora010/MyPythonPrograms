# create a variable outside a function , and use it inside the function
a="krushna"

def myfunc():
    print("hello good morning " + a)

myfunc()

# create a variable inside a function , with the same name as the global variable
x="krushna"

def myfunction():
    x="ganesh"
    print("hii hello good morning " + x)
myfunction()
print("what are you doing " + x)


