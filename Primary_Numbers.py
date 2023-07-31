import math


def compute_primary_number(n):
    prime_count = 0
    primary_list = []
    current = 2
    while True:
        if prime_count == n:
            break
        isPrime = True
        print(math.ceil(math.sqrt(current)))
        for i in range(2, math.ceil(math.sqrt(current + 1))):
            if current % i == 0:
                isPrime = False
                break
        if isPrime:
            primary_list.append(current)
            prime_count = prime_count + 1
        current = current + 1
        print(current)
    return primary_list


prime_num = compute_primary_number(20)
print(prime_num)
