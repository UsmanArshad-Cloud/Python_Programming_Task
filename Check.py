def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("Decorator: Before calling the function")
        result = func(*args, **kwargs)
        print("Decorator: After calling the function")
        return result
    return wrapper

@my_decorator
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

result = factorial(5)
print("Factorial of 5 is:", result)
