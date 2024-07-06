#  Can we have a set with 18 (int) and '18' (str) as a value in it?

new=set()
a=input("Enter value of a:")
new.add(a)
b=input("Enter value of b:")
new.add(int(b))
print(new)