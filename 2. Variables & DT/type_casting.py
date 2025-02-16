# From one data type to another
a = int("100")
b = int("200")
c = a + b
print(c)

# STRING -> INTEGER
# INT wont know what does decimal mean
a = int("100.1")
print(a)

# FLOAT -> INT:
# It will take the whole number mentioned i.e. remove the decimal
# OR number nearest to 0

b = int(100.9)
# It can be either 100 or 101. Nearer to 0 is 100, so 100
print(b)
d = int(-5.67)  # Either -5 or -6 but nearest one is -5
print(d)
