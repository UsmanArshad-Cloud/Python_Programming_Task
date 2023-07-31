def compute_bitwise(a,b):
    bitwise_and=a&b
    bitwise_or=a|b
    bitwise_xor=a^b
    return bitwise_and,bitwise_or,bitwise_xor

def leftshift_and_rightshift(number):
    left_shift_result=number<<1
    right_shift_result=number>>1
    return left_shift_result,right_shift_result

def multiply_number_by_10_using_shift(num):
    multiply_8_result = (num << 2)+(num << 2)
    multiply_2_result=num<<1
    multiply_10_result=multiply_8_result+multiply_2_result
    print(multiply_10_result)


a = int(input("Give first: "))
b = int(input("Give Second: "))
and_result,or_result,xor_result = compute_bitwise(a,b)
print(f"The bitwise representation of a is {bin(a)} and of b is {bin(b)} ")
print(f"The result of and,or and xor operation is {and_result},{or_result},{xor_result} respectively")

left_shift_result,right_shift_result=leftshift_and_rightshift(10)
print(left_shift_result)
print(right_shift_result)
multiply_number_by_10_using_shift(10)