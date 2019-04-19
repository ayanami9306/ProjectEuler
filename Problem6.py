count = 1
list = [2]
num = 3
while count < 10001:
    Flag = True
    for list_i in list:
        if num % list_i == 0:
            Flag = False
            break
    if Flag == True:
        list.append(num)
        count += 1
    num += 2
print(list[-1])
