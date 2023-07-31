from functools import reduce

array = [10, 7, 8]


def findMaximum(x, y):
    return y if x > y else x


array.remove(reduce(findMaximum, array))
print(array)
