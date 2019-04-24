# 40 C 20
value = 1
for i in range(1, 21):
    value *= (i+20)/i
print(int(value+0.5))