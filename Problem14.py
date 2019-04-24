a = {1: 1, 2: 2}
for i in range(3, 1000000):
    count = 0
    num = i
    while i != 1:
        if i in a:
            count += a[i]
            break
        count += 1
        if i % 2 == 0:
            i = int(i / 2)
        else:
            i = i * 3 + 1
    a[num] = count
max_value = 0
max_key = 1
for i in a:
    if a[i] > max_value:
        max_key = i
        max_value = a[i]
print(max_key)