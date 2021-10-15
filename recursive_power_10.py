def recursive_power(number, power, result = 1):
    result *= number
    if power == 1:
        return result
    return recursive_power(number, power-1, result)

# print(2**10)


print(recursive_power(2, 10))
print(recursive_power(10, 100))