"""ask number and print factors
three ways: brut force, better, optimal"""

# BRUT FORCE: WHAT COMES IN MIND
# a = int(input("enter number"))
# num = a
# start = 1
# while start <= num:
#     if num % start == 0:
#         print(start, end=" ")
#     start += 1

""" AS number increases no of times loop runs also increases
here it will run 10000 times if 10000 is number.

instead: ex: 20 is number
1,2,4,5,10,20 are its factors

30 is number
1,2,3,5,6,10,15,30 are ita factors

we see half of numebr, tehre are no more factors 
beyond this number except number itself
"""

# a = int(input("enter number"))
# num = a
# for i in range(1, num // 2 + 1):
#     if num % i == 0:
#         print(i, end=" ")
# print(a)  # so thta number itself joins

""" Now time complexity is N/2 as code runs half times
so better than original.
now: 36
1--36
2--18
3--12
4--9
5 )NA(
6--6
so loop must go till 6 only i.e.  underoot36
"""

# a = int(input("enter number"))
# num = a
# for i in range(1, int((num**0.5) + 1)):
#     if num % i == 0:
#         print(i, end=" ")
#         if num // i != i:  # for 36: 36/6=6 if this not mrntioned 6 will come twice
#             print(num // i, end=" ")


""" prime composite number"""

# a = int(input("enter number"))
# num = a
# count_f = 0
# factors = []

# for i in range(1, int((num**0.5) + 1)):
#     if num % i == 0:
#         factors.append(i)
#         if num // i != i:
#             factors.append(num // i)
#             count_f += 1
# if count_f > 2:
#     print(f"The number {a} is composite number and its factors are {factors}")
# else:
#     print(f"The number {a} is prime number with factors: {factors}")

""" to optimise it more"""
a = int(input("enter number"))
num = a
count_f = 0
factors = []

for i in range(1, int((num**0.5) + 1)):
    if num % i == 0:
        count_f += 1
        if num // i != i:
            count_f += 1
            if count_f > 2:
                break
if count_f > 2:
    print("not prime")
else:
    print("prime")

""" time complexity: underoot n-- optimised"""
