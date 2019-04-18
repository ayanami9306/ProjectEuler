max_value = 0
for i in range(999, 99, -1):
    for j in range(999, 99, -1):
        num = i * j
        num_list = str(num)
        if num_list == num_list[::-1]:
            if max_value < num:
                max_value = num
print(max_value)