import numpy as np
abundant_number = []

for i in range(1, 28123):
    sum_divisors = 1
    for j in range(2, int(i**0.5)+1):
        if i % j == 0:
            sum_divisors += j
            multiplier = int(i/j)
            if multiplier != j:
                sum_divisors += multiplier
    if sum_divisors > i:
        abundant_number.append(i)

numbers = set(range(1, 28123))

for index, i in enumerate(abundant_number):
    for j in abundant_number[index:]:
        if (i+j) in numbers and i+j <28123:
            numbers.remove(i+j)

print(sum(numbers))