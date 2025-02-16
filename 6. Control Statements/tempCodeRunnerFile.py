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
