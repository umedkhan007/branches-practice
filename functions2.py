#succesfully merged

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

# Example usage
num = 5
result = factorial(num)
print(f"The factorial of {num} is {result}")

#2

def sum_of_list(numbers):
    return sum(numbers)

# Example usage
numbers = [1, 2, 3, 4, 5]
result = sum_of_list(numbers)
print(f"The sum of the list is {result}")

#3
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Example usage
num = 7
result = is_prime(num)
print(f"Is {num} prime? {result}")


#4
def reverse_string(s):
    return s[::-1]

# Example usage
string = "hello"
reversed_string = reverse_string(string)
print(f"The reversed string is {reversed_string}")
