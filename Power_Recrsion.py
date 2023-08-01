from functools import wraps
def Power_Iterative(base, exponent):
    result = 1
    for i in range(exponent):
        result *= base
    print(result)


# Power_Iterative(2,5)


def Power_Recursive_n(base, exponent):
    if exponent == 0:
        return 1

    return base * Power_Recursive_n(base, exponent - 1)


# print(Power_Recursive_n(2,5))


def Power_Recursive_logn(base, exponent):
    isExpNegative = False
    if exponent < 0:
        exponent = abs(exponent)
        isExpNegative = True
    if exponent == 0:
        return 1
    if exponent % 2 == 0:
        return Power_Recursive_logn(base, exponent / 2) * Power_Recursive_logn(base, exponent / 2) if not isExpNegative \
            else 1 / (Power_Recursive_logn(base, exponent / 2) * Power_Recursive_logn(base, exponent / 2))
    else:
        return 1 / (base * Power_Recursive_logn(base, exponent - 1)) if isExpNegative \
                else base * Power_Recursive_logn(base, exponent - 1)


def decorator_func(func):
    def wrapper(*args, **kwargs):
        base = args[0] if args[1] > 0 else 1/args[0]
        exponent = abs(args[1])
        result = func(base, exponent)
        return result
    return wrapper


@decorator_func
def power_recursive_simplified(base, exponent):
    if exponent == 0:
        return 1
    if exponent % 2 == 0:
        return Power_Recursive_logn(base, exponent / 2) * Power_Recursive_logn(base, exponent / 2)
    else:
        return base * Power_Recursive_logn(base, exponent - 1)


print(Power_Recursive_logn(2, 5))  # 32
print(Power_Recursive_logn(-2, 7))  # -128
print(Power_Recursive_logn(2, -5))  # 0.03125
print(Power_Recursive_logn(-2, -9))  # -0.001953125

print(power_recursive_simplified(2, 5))  # 32
print(power_recursive_simplified(-2, 7))  # -128
print(power_recursive_simplified(2, -3))  # 0.125
print(power_recursive_simplified(-2, -9))  # -0.001953125