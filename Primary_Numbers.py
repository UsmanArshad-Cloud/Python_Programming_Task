import math


def compute_primary_number(n):
    prime_count = 0
    primary_list = []
    current = 2
    while prime_count < n:
        isPrime = True
        for i in range(2, math.ceil(math.sqrt(current + 1))):
            if current % i == 0:
                isPrime = False
                break
        if isPrime:
            primary_list.append(current)
            prime_count = prime_count + 1
        current = current + 1
    return primary_list


prime_num = compute_primary_number(100)
print(prime_num)
