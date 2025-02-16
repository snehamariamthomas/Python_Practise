""" Anything after continue within while not be executed """

i = 1
while i <= 20:
    print(i)
    if i == 5:
        continue
    i += 1

# SInce after continut i is not being incremeneted so 1 2 3 4 5 5 5 5....
