def double_num(num):
    return num * 2


array = [1, 2, 3, 4, 5]

doubled_array = list(map(double_num, array))

print(doubled_array)

# create list of object with 2 keys {a:1,b:2} and add 1 more key c:3 using map function


def append_c(dict):
    dict["c"] = 3
    return dict


input_list = [{"a": 1, "b": 2},{"a":1, "b":2}]
final_list = list(map(append_c,input_list))
print(final_list)
