a = int(input("Enter start number"))
b = int(input("Enter end number"))

i = a
j = b


if i < j:
    for k in range(i, j + 1):
        print(k, end=" ")
else:
    for k in range(i, j - 1, -1):
        print(k, end=" ")
