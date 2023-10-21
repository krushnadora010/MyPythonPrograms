# program to reverse a string/(using slice method)
var1= "krushna"
print(var1[::-1])

# reverse a string by using built in join and reversed function.

var2= "jay bira hanuman"
var2= "".join(reversed(var2))
print(var2)

#  function to reverse string.

def reverse(string):
    string="".join(reversed(string))
    return string
s="m krushna chandra dora"
print("the original string is :", end="")
print(s)

print("the reverse string is:", end="")
print(reverse(s))

# reverse string in python using list comprehession.

def reverse(string):
    string=[string[i] for i in range(len(string)-1,-1,-1)]
    return "".join(string)
s="geeksforgeeks"
print("the original string is :",s)
print("the reverse string is :",reverse(s))
