def Power_Iterative(base,exponent):
    result=1
    for i in range(exponent):
        result*=base
    print(result)

Power_Iterative(2,5)


def Power_Recursive_n(base,exponent):
    if exponent==0:
        return 1

    return base*Power_Recursive_n(base, exponent-1)

print(Power_Recursive_n(2,5))

def Power_Recursive_logn(base,exponent):
    if exponent==0:
        return 1
    if exponent%2==0:
        return Power_Recursive_logn(base,exponent/2)*Power_Recursive_logn(base,exponent/2)
    else:
        return base*Power_Recursive_logn(base,exponent-1)

print(Power_Recursive_logn(2,5))
print(Power_Recursive_logn(2,4))
