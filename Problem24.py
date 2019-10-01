import math

sum_order = 1000000
indexes = []
total_digits = list(range(10))
while sum_order > 0:
    for i in total_digits:
        temp_fac = math.factorial(len(total_digits)-1)
        if temp_fac < sum_order:
            sum_order -= temp_fac
        else:
            indexes.append(i)
            total_digits.remove(i)
            if sum_order == temp_fac:
                if len(total_digits) == 0:
                    sum_order -= temp_fac
            break

print(indexes)