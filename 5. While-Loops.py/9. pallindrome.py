num = int(input("enter number"))
n = num
sums = 0
while n > 0:
    ld = n % 10
    n = n // 10
    sums = (sums * 10) + ld
if sums == num:
    print("Pallindrome, yay!")
else:
    print("Sorry, not a pallindrome!")
