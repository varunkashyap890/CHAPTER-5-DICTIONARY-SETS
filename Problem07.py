# If the names of 2 friends are same; what will happen to the program in problem 6?


d={}
name=input("Enter your name:")
language=input("Enter your language:")
d.update({name:language})
name=input("Enter your name:")
language=input("Enter your language:")
d.update({name:language})
name=input("Enter your name:")
language=input("Enter your language:")
d.update({name:language})
name=input("Enter your name:")
language=input("Enter your language:")
d.update({name:language})
print(d,type(d))


# Note if the name of friend and language are same then length of dictionary will be 3