def power(base , expo) :
    if expo == 0:
        return 1
    else:
        return base * power(base, expo - 1)

print(power(2, 0))
print(power(2, 2))
print(power(2, 4))
