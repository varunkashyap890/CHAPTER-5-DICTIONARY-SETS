# Create an empty dictionary. Allow 4 friends to enter their favorite language as 
# value and use key as their names. Assume that the names are unique.

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