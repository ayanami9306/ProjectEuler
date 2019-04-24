num = 0
adder = 1
while True:
    num += adder
    adder += 1
    divisor = []
    for i in range(1, int(num**0.5)+1):
        if num % i == 0:
            divisor.append(i)
            temp = num / i
            if temp != i:
                divisor.append(temp)
    if len(divisor) > 500:
        break
print(num)