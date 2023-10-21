vowels=['a','e','i','o','u']
word=input("enter the word to search for vowles: ")
found=[]
for letter in word:
    if letter in vowels:
        if letter not in found:
            found.append(letter)
print(found)
print('the number of different vowles present in ',word,'is',len(found))
            