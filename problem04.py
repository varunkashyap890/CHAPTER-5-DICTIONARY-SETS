# What will be the length of following set s:
# s = set()
# s.add(20)
# s.add(20.0)
# s.add('20') # length of s after these operations?
s=set()
a=int(input("Enter value of a=18 as 'int':"))
s.add(a)
b=float(input("Enter value of b=18 as 'float':"))
s.add(b)
c=input("Enter value of C=18 as 'string':")
s.add(c)
print(s)