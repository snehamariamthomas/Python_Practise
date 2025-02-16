# Ask a positive number from user. Print from 1 to n
# n = int(input("Enter a number"))
# i = 1
# while i <= n:
#     print(i)
#     i += 1


# Ask a positive number from user. Calculate the total sum of all the
# numbers from 1 to n.

# n = int(input("Enter a number"))
# i = 1
# sum = 0
# while i <= n:
#     sum += i
#     i += 1
# print(sum)


# Q3. Ask a start number and end number from user. Calculate the total sum
# of all the numbers from start to end.
# start = int(input("Enter starting number"))
# end = int(input("Enter ending number"))

# i = start
# sum = 0
# while i <= end:
#     sum += i
#     i += 1
# print(sum)


# Q4. Ask a positive number from user. Print from n to 1
# start = int(input("Enter starting number"))

# while start > 0:
#     print(start, end=" ")
#     start -= 1

# Ask a positive number from user. Print from n to -n.
# start = int(input("Enter starting number"))
# end = -1 * start
# i = start
# while i >= end and i <= start:
#     print(i, end=" ")
#     i -= 1

""" 
n = int(input("Enter a positive number = "))
i = n
while i >= -n:
    print(i, end=" ")
    i -= 1
    """

# Q6. Print all the numbers divisible by 2, 3 and 5 from start to end. Ask start
# and end numbers from the user.

# start = int(input("Enter starting number"))
# end = int(input("Enter ending number"))

# i = start
# while i <= end:
#     i += 1
#     if i % 2 == 0 and i % 3 == 0 and i % 5 == 0:
#         print(i, end=" ")

# Ask a number from user. Print the multiplication table of that number.
# n = int(input("Enter number for multiplication table "))
# i = 1
# product = 1
# while i <= 10:
#     product = n * i
#     print(f"{n} * {i} = {product}")
#     i += 1

# Ask a start number and end number from user. Ask another number n
# from the user. Print all the numbers from start to end divisible by n.

# start = int(input("Enter starting number"))
# end = int(input("Enter ending number"))
# n = int(input("Enter divisibility number"))

# i = start
# while i <= end:
#     if i % n == 0:
#         print(i, end=" ")
#     i += 1

# . Count the number of odd and even numbers from start to end. Ask
# start and end number from user.

# start = int(input("Enter starting number"))
# end = int(input("Enter ending number"))
# odds = 0
# evens = 0
# i = start
# while i <= end:
#     if i % 2 == 0:
#         evens += 1
#     else:
#         odds += 1
#     i += 1
# print(f"Number of odds is {odds}")
# print(f"Number of evens is {evens}")


# Ask two number from user that is start and end. Also start can be
# greater or smaller than the end number. Print from start to end. See the
# examples below.

# start = int(input("Enter starting number"))
# end = int(input("Enter ending number"))
# i = start
# j = end
# if i < j:
#     while i <= j:
#         print(i, end=" ")
#         i += 1
# else:
#     while i >= j:
#         print(j, end=" ")
#         j += 1

""" 
start = int(input("Enter start number = "))
end = int(input("Enter end number = "))

if start > end:
    temp = start
    start = end
    end = temp

i = start

while i <= end:
    print(i, end=" ")
    i += 1

"""


# Q11. Print the following pattern. Ask n from user.
# Example 1:
# Enter n = 6
# Output:
# 1 2 4 8 16 32
# Example 1:
# Enter n = 10
# Output:
# 1 2 4 8 16 32 64 128 256 512

# n = int(input("Enter  number"))
# i = 1
# prod = 1
# while i <= n:
#     print(prod, end=" ")
#     prod = prod * 2
#     i += 1


# Q12. Print the following pattern. Ask n from user.
# Example 1:
# Enter n = 5
# Output:
# 1 11 111 1111 11111

# n = int(input("Enter  number"))
# i = 1
# while i <= n:
#     print("1" * i, end=" ")
#     i += 1

"""n = int(input("Enter a number = "))

i = 1
number = 1

while i <= n:
    print(number)
    number = number * 10 + 1
    i += 1"""
