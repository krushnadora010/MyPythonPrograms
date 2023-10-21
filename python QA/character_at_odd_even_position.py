# write a program to print characters at odd position and even position for the given string ?

# first way
str=input("enter your string:")
print("character at even position:",str[0::2])
print("character at even position:",str[1::2])

#second way
s=input("enter your string: ")
i=0
print("character at even position")
while i<len(s):
    print(s[i],end=',')
    i=i+2
print()
i=1
print("character at odd position")
while i<len(s):
    print(s[i],end='')
    i=i+2
