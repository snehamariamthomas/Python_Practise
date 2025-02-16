""" Write a program to calculate the factorial of a
given number using a loop"""

# a = int(input("enter a number"))
# num = a
# product = 1
# for i in range(num, 0, -1):
#     product *= i
# print(f" the factorial of {a} is {product}")


""" Ask a number from user. Print all the factors of a that number. (Order
does not matter, just print it"""

# a = int(input("enter a number"))
# num = a

# for i in range(1, int((num**0.5) + 1)):
#     if num % i == 0:
#         print(i, end=" ")
#         if num // i != i:
#             print(num // i, end=" ")


""" Ask a number from user. Count the number of factors of that number"""

# a = int(input("enter a number"))
# num = a
# count_f = 0

# for i in range(1, int((num**0.5) + 1)):
#     if num % i == 0:
#         count_f += 1
#         if num // i != i:
#             count_f += 1
# print(f" the total factors of {a} are {count_f}")


""" Ask a number from user. Print the sum of all the factors of that number"""

# a = int(input("enter a number"))
# num = a
# sum_f = 0

# for i in range(1, int((num**0.5) + 1)):
#     if num % i == 0:
#         sum_f += i
#         if num // i != i:
#             sum_f += num // i
# print(f" the sum of factors of {a} are {sum_f}")

""" Ask a number from user. Print Yes if that number is a prime number
else print No"""

# a = int(input("enter a number"))
# num = a
# count_f = 0

# for i in range(1, int((num**0.5) + 1)):
#     if num % i == 0:
#         count_f += 1
#         if num // i != i:
#             count_f += 1
#             if count_f > 2:
#                 break
# if count_f > 2:
#     print("Composite Number")
# else:
#     print("Prime Number")

""" Write a program to check if a given number is a perfect number. A
number is called perfect if it is equal to the sum of its proper divisors
(divisors excluding the number itself)."""

# a = int(input("enter a number"))
# num = a
# factors = []

# for i in range(1, ((num // 2) + 1)):
#     if num % i == 0:
#         factors.append(i)
# print(factors)
# if sum(factors) == a:
#     print(f" {a} is a perfect number")
# else:
#     print(f" {a} is not a perfect number")

"""ASSIGNMENT ANSWER"""

# n = int(input("Enter a number = "))
# sum_of_divisors = 0
# for i in range(1, n):
#     if n % i == 0:
#         sum_of_divisors += i
# if sum_of_divisors == n:
#     print(True)
# else:
#     print(False)

""" Write a program to repeatedly sum the digits of a number until only a
single-digit number is obtained. The process involves summing the digits
of the number and then repeating the process with the result until the
number is reduced to a single digit.

Requirements:
1. You are given a positive integer n (Ask n from user)
2. You need to find the sum of the digits of n, and if the result is greater
than 9, repeat the process.
3. Continue summing the digits until the result is a single-digit number.
4. Do not use lists, strings, dictionaries, or nested loops.

Example Scenarios to Consider:
1. Input: 9875
Output: 2
Explanation:
Step 1: 9 + 8 + 7 + 5 = 29
Step 2: 2 + 9 = 11
Step 3: 1 + 1 = 2 (single digit obtained)."""

# a = int(input("enter a number"))
# num = a
# digit = 0
# while num > 0:
#     digit += num % 10
#     num = num // 10
# while digit > 9:
#     num = digit
#     digit = 0
#     while num > 0:
#         digit += num % 10
#         num = num // 10
# else:
#     print(digit)

""" assignment answer"""

a = int(input("enter a number"))
num = a
while num >= 10:
    sums = 0
    while num > 0:
        sums += num % 10
        num = num // 10
    num = sums
print(num)
