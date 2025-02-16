""" Keep asking user question untill he inputs 0 
and show sum  of all questions inputted"""

# sum = 0

# while True:  # when you dont know how many times to be run
#     i = int(input("Enter a number"))
#     sum += i
#     if i == 0:
#         break

# print(f"The sum is {sum}")


""" Keep asking user question untill he inputs 0 
and show sum and average of all questions inputted"""

sums = 0  # Initialize sum
count = 0  # Initialize count

while True:
    i = int(input("Enter a number: "))
    if i == 0:  # Stop when user enters 0
        break
    sums += i
    count += 1

# Ensure we don't divide by zero
average = sums / count if count > 0 else 0

print(f"The total is {sums}, count is {count}, and average is {average}")
