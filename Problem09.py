# Can you change the values inside a list which is contained in set S?
# s = {8, 7, 12, "Harry", [1,2]}


s = {8, 7, 12, "Harry", [1,2]}  # list are not hashable,tuples are hashable
print(s)



t = {8, 7, 12, "Harry", (1,2)}
print(t)
