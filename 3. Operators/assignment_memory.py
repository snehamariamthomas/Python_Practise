a = 5
print(id(a))  # 140732751628856

a += 3  # a=a+3
print(a)
print(id(a))  # 140732751628952

# CASE 2
a = 5
b = 5
print(f" a = {a} and id is {id(a)}")
print(f" b = {b} and id is {id(b)}")
# BOTH HAVE SAME ID
""" When there is a number , here 5,
it will be stored in memory with a id. when we assign it to a
it will poin to the address which has 5.
now when b is created, it wont waste memory by creating new place for 5.
again b will point to address which has 5.
Hence both have same id"""
