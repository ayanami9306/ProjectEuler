prime_list = [2, 3]
count = 2
num = 3
while count < 10001:
    num += 2
    Flag = True
    for prime_i in prime_list:
        if num % prime_i == 0:
            Flag = False
            break
    if Flag:
        prime_list.append(num)
        count += 1
print(num)