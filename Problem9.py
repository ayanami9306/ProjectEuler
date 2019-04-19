for a in range(1, 999):
    for b in range(1, a+1):
        c = 1000 - a - b
        if c**2 == a**2 + b**2:
            print(a*b*c)
            exit(0)