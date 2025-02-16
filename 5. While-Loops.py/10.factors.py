num = int(input("Enter number"))
n = num
i = 1
while i <= num:
    if num % i == 0:
        print(i, end=" ")
    i += 1
