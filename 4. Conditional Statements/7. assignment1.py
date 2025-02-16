# Q1. Ask a number from user. Print Even or Odd
# num = int(input("Enter a number"))
# if num % 2 == 0:
#     print("Even")
# else:
#     print("Odd")

# Q2. Ask a number from user. Print Positive, Negative or Zero.
# num = int(input("Enter a number"))
# if num > 0:
#     print("Positive")
# elif num < 0:
#     print("Negative")
# else:
#     print("Zero")

# Ask a number from user. Print Yes if the number is divisible by 2,3 and
5
# num = int(input("Enter a number"))
# if num % 2 == 0 and num % 3 == 0 and num % 5 == 0:
#     print("Yes")
# else:
#     print("No")

# Q4. Write a Python program that accepts an integer number from the user
# and classifies it as:
# Positive and Even
# Positive and Odd
# Negative and Even
# Negative and Odd
# Zero

# num = int(input("Enter a number"))
# if num > 0:
#     if num % 2 == 0:
#         print("Positive and Even")
#     else:
#         print("Positive and Odd")
# elif num < 0:
#     if num % 2 == 0:
#         print("Negative and Even")
#     else:
#         print("Negative and Odd")
# else:
#     print("Zero")

# Write a Python program that accepts a student's marks in three
# subjects and prints the grade based on the following conditions:
# Marks > 90: Grade A
# 80 < Marks <= 90: Grade B
# 70 < Marks <= 80: Grade C
# 60 < Marks <= 70: Grade D
# Marks <= 60: Fail

# m1 = int(input("Enter first marks"))
# m2 = int(input("Enter second marks"))
# m3 = int(input("Enter third marks"))
# per_marks = ((m1 + m2 + m3) / 300) * 100

# if per_marks >= 90:
#     print(f"Grade A and percentage: {per_marks}")
# elif per_marks < 90 and per_marks >= 80:
#     print(f"Grade B and percentage: {per_marks}")
# elif per_marks < 80 and per_marks >= 70:
#     print(f"Grade C and percentage: {per_marks}")
# elif per_marks < 70 and per_marks >= 60:
#     print(f"Grade D and percentage: {per_marks}")
# else:
#     print(f"Fail and percentage: {per_marks}")


# Write a program to find the maximum and minimum of three numbers
# entered by the user using if-else statements.

# num1 = int(input("Enter number 1 = "))
# num2 = int(input("Enter number 2 = "))
# num3 = int(input("Enter number 3 = "))

# # Find maximum
# if num1 >= num2 and num1 >= num3:
#     maximum = num1
# elif num2 >= num1 and num2 >= num3:
#     maximum = num2
# else:
#     maximum = num3

# # Find minimum
# if num1 <= num2 and num1 <= num3:
#     minimum = num1
# elif num2 <= num1 and num2 <= num3:
#     minimum = num2
# else:
#     minimum = num3

# print(
#     f" The numbers are {num1},{num2} and {num3}. Max is {maximum} and Min is {minimum}"
# )

# Write a Python program that calculates the BMI and classifies it based
# on the following conditions:
# BMI < 18.5: Underweight
# 18.5 <= BMI < 24.9: Normal weight
# 25 <= BMI < 29.9: Overweight
# BMI >= 30: Obesity
# BMI is calculated as weight(kg) / height(m)^2
# Input: Weight in kg and Height in meters (e.g., 70, 1.75)
# Output: Normal weight

# weight = int(input("Weight in kg"))
# height = int(input("Height in meters"))
# bmi = weight / (height**2)
# if bmi < 18.5:
#     print("Underweight")
# elif bmi >= 18.5 and bmi <= 24.9:
#     print("Normal weight")
# elif bmi >= 25 and bmi <= 29.9:
#     print("Overweight")
# else:
#     print("Overwieght")


# weight = float(input("Enter your weight in kg = "))
# height = float(input("Enter your height in meters = "))

# # Calculate BMI
# bmi = weight / (height**2)

# if bmi < 18.5:
#     print(f"Your BMI is {bmi:.2f}. You are Underweight.")
# elif 18.5 <= bmi < 24.9:
#     print(f"Your BMI is {bmi:.2f}. You have a Normal weight.")
# elif 25 <= bmi < 29.9:
#     print(f"Your BMI is {bmi:.2f}. You are Overweight.")
# else:
#     print(f"Your BMI is {bmi:.2f}. You have Obesity.")

# Write a Python program to determine if a student is eligible for college
# admission based on the following criteria:
# Minimum score in Math: 70
# Minimum score in Science: 65
# Minimum score in English: 60
# Total score across all subjects: 200

# math = int(input("Enter Math"))
# science = int(input("Enter Science marks"))
# english = int(input("Enter English marks"))
# total = math + science + english

# if total >= 200:
#     if math >= 70 and science >= 65 and english >= 60:
#         print("Yes, Admitted!")
#     else:
#         print("Sorry,better luck next time")
# else:
#     print("Sorry,better luck next time")
