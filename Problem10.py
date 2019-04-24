prime_list = [0] * 2000000
prime_list = [2, 3] + prime_list
num = 5
count = 2
while num <= 2000000:
    Flag = True
    sqrt_num = num**0.5
    for prime_i in prime_list[0:count]:
        if prime_i > sqrt_num:
            break
        if num % prime_i == 0:
            Flag = False
            break
    if Flag:
        prime_list[count] = num
        count += 1
    num += 2
print(sum(prime_list[0:count]))