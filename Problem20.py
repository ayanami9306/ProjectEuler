factorial = 1
for i in range(1, 101):
    factorial *= i
factorial = str(factorial)
sum = 0
for i in factorial:
    sum += int(i)
print(sum)