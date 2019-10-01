Fn = [1, 1, 2]
count = 3
while len(str(Fn[2])) < 1000:
    temp = [Fn[1], Fn[2], Fn[1]+Fn[2]]
    Fn = temp
    count += 1

print(count)