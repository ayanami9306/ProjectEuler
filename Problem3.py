num = 600851475143
i = 2
while num != i:
    if num % i == 0:
        num /= i
    else:
        i += 1
print(num)