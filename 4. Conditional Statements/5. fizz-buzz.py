num = int(input("Enter a number"))

# MY ATTEMPT
if num % 2 == 0 and num % 3 != 0:
    print("FIZZ")
elif num % 2 != 0 and num % 3 == 0:
    print("BUZZ")
elif num % 2 == 0 and num % 3 == 0:
    print("FIZZBUZZ")
else:
    print("FIZZFIZZBUZZBUZZ")

# CHECK IN FIRST CONDITION ITSELF IF DIVISIBLE BY BOTH THEN INDIVIDUAL CHECK

if num % 2 == 0 and num % 3 == 0:
    print("FIZZBUZZ")
elif num % 2 == 0:
    print("FIZZ")
elif num % 3 == 0:
    print("BUZZ")
else:
    print("FIZZFIZZBUZZBUZZ")
