""" 
num=1234
reverse= 4321
"""

n = 1234
sum = 0
num = n
while num > 0:
    dig = num % 10
    sum = (sum * 10) + dig
    num = num // 10
print(sum)
