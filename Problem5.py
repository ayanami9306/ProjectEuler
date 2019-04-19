dict = {2: 0, 3: 0, 5: 0, 7: 0, 11: 0, 13: 0, 17: 0, 19: 0}
keyvalue = [2, 3, 5, 7, 11, 13, 17, 19]
for i in range(2, 21, 1):
    num = i
    for key_i in keyvalue:
        key_count = 0
        while num % key_i == 0:
            num /= key_i
            key_count += 1
        if key_count > dict[key_i]:
            dict[key_i] = key_count
sum = 1
for key_i in keyvalue:
    if dict[key_i] != 0:
        sum *= key_i ** dict[key_i]
print(sum)