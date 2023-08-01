def compute_bitwise(a, b):
    bitwise_and = a & b
    bitwise_or = a | b
    bitwise_xor = a ^ b
    return bitwise_and, bitwise_or, bitwise_xor


def leftshift_and_rightshift(number):
    left_shift_result = number << 1
    right_shift_result = number >> 1
    return left_shift_result, right_shift_result


def multiply_number_by_10_using_shift(num):
    multiply_8_result = (num << 2) + (num << 2)
    multiply_2_result = num << 1
    multiply_10_result = multiply_8_result + multiply_2_result
    print(multiply_10_result)


# a = int(input("Give first: "))
# b = int(input("Give Second: "))
# and_result,or_result,xor_result = compute_bitwise(a,b)
# print(f"The bitwise representation of a is {bin(a)} and of b is {bin(b)} ")
# print(f"The result of and,or and xor operation is {and_result},{or_result},{xor_result} respectively")
#
# left_shift_result,right_shift_result=leftshift_and_rightshift(10)
# print(left_shift_result)
# print(right_shift_result)
# multiply_number_by_10_using_shift(10)


"""
we need to write a program where we can return the set bits of a number
100= set bids is 1
1010 = set bids 2
we need to pass an integer number and we will return the set bits count of that number binary
"""


def return_set_bits(n):
    binary = bin(n)
    parsed_binary = binary[2:]
    print(f"Binary Representation of the given integer is {parsed_binary}")
    index = 0
    one_count = 0
    if parsed_binary[0] == '1':
        one_count += 1
    while index != -1:
        index = parsed_binary.find("1", index + 1, len(parsed_binary))
        if index != -1:
            one_count += 1
    return one_count


def return_set_bits_using_shift(n):
    result = n
    ones_count = 0
    while result != 0:
        result_bit = bin(result)
        if result_bit[-1] == '1':
            ones_count += 1
        result = result >> 1
    return ones_count


# count = return_set_bits(10)
input_val = int(input("Give Number in Decimal"))
count2=return_set_bits_using_shift(input_val)  # 4
print(f"Count of set bits in {input_val} is {count2}")
