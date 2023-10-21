def fun(name,age,mark,contact):
    print(name,age,mark,contact)
list=["krushna",22,70,9827377082]
fun(*list)    

#example:-2

args=["rajesh",20,70,8373477348]

def func(name,age,mark):
    return name,age,mark

func(*args)