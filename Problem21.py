import numpy as np
sum_divisors = np.full((10001), 1)

for i in range(1, 10001):
    for j in range(2, int(i**0.5)+1):
        if i % j == 0:
            sum_divisors[i] += j
            multiplier = int(i/j)
            if multiplier != j:
                sum_divisors[i] += multiplier

sum = 0
for i in range(1, 10001):
    if sum_divisors[i] <= 10000:
        if i == sum_divisors[sum_divisors[i]] and i != sum_divisors[i]:
            sum += i

print(sum)

