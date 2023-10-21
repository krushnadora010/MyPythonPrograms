def pyramid(n):
    for i in range(0,n):
        for j in range(0,i+1):
            print("*",end="")
        print("\r")
n=5
pyramid(n)    

print()
def pyramid(n):
    for i in range(0,n):
        for j in range(0,i+1):
            print("*",end="")
        print("\n")
n=5
pyramid(n)    