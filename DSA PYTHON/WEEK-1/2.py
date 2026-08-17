def power(base, exp):
    if exp < 0:
        return 1 / power(base, -exp)
    if exp == 0:
        return 1
    return base * power(base, exp - 1)
print(power(23000,3))
print(power(2503,-1))
print(power(513,0))
