num = int(input("enter a number"))

# if num % 2 == 0:
#     print(f"The number provided is {num} and it is even")
# else:
#     print(f"The number provided is {num} and it is odd")

if (
    num % 2
):  # say 20%2=0--> Falsly so will go to else # if 21%2=1->Truthly then print odd
    print("Odd")
else:
    print("Even")
