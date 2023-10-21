list=[1,2,3,4,5,6,7,8,9,10]
i=0
while(i<len(list)):
    print(list[i])
    i=i+1

list1=[1,2,3,4,5,6,7,8,9,10]
for i in list1:
    print(i)

# to display only even number
list2=[1,2,3,4,5,6,7,8,9,10]
for i in list2:
    if (i%2==0):
        print(i)

# to display elements by index wise
list3=['A','B','C','D','E']
a=len(list3)
for i in range(a):
    print(list3[i],"is availablle at positive index: ",i,"and at negative index :",i-a)


# to add all elements to list upto 100 which are divisible by 10
list=[]
for i in range(101):
    if i%10==0:
        list.append(i)
print(list)

#using insert function
# to insert item at specified index position
list1=[5,3,8,1,9,3,2]
list1.insert(3,50)
print(list1)

list1=[5,3,8,1,9,3,2]
list1.insert(20,50)
list1.insert(-30,100)
print(list1)

# using extend function
order1=["chicken","mutton","fish","egg"]
order2=["black bakadi","bakadi lemon","black dog"]
order1.extend(order2)
print(order1)

order1=["chicken","mutton","fish","egg"]
order1.extend("mushroom")
print(order1)

# using remove function
n=[10,20,30,40,50]
n.remove(20)
print(n)

# using pop function
order1=["chicken","mutton","fish","egg"]
print(order1.pop())
print(order1.pop())
print(order1)


n=[40,10,20,30]
n.sort()
print(n)
n.sort(reverse=True)
print(n)
n.sort(reverse=False)
print(n)

