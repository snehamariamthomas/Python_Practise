# total = 0
# i = 1
# while i <= 10:
#     total += i
#     i += 1
# print(total)


start = int(input("Enter start"))
end = int(input("Enter end"))

i = start
sums = 0
while i <= end:
    if i % 2 == 0 and i % 7 == 0:
        sums += i
    i += 1
print(sums)
