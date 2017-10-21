def GCD(a, b):
    if b == 0:
        return a
    else:
        return GCD(b, a % b)

print(GCD(24, 18))
print(GCD(8, 16))
print(GCD(11, 244))
