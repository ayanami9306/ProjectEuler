month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
# Year 1900 has 365days (not leap year) :
# 52 weeks and 1 days : 1 Jan 1901 is Tuesday
day = 1
sum_sundays = 0
for i in range(1901, 2001):
    for j in month_days:
        if day == 6:
            sum_sundays += 1
        day += j
        if j == 28 and (i % 4 == 0 and (i % 100 != 0 or i % 400 == 0)):
            day += 1
        day -= (int(day/7) * 7)
print(sum_sundays)