nums = [1, 2, 3, 4, 5]
squares = list(map(lambda x: x ** 2, nums))
print(squares)  # Output: [1, 4, 9, 16, 25]


def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()


def filter_even_squares(nums):
    return [x**2 for x in nums if x % 2 == 0]

numbers = [1, 2, 3, 4, 5, 6]
print(filter_even_squares(numbers))  # Output: [4, 16, 36]



def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(5))  # Output: 120

