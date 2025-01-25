# 1. Function to check if a number is even or odd
def is_even_or_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"

# 2. Function to find the largest of three numbers
def find_largest(a, b, c):
    return max(a, b, c)

# 3. Function to calculate the square of a number
def square(num):
    return num ** 2

# 4. Function to reverse a string
def reverse_string(s):
    return s[::-1]

# 5. Function to calculate the area of a rectangle
def rectangle_area(length, width):
    return length * width

# Testing the functions
print(f"Is 7 even or odd? {is_even_or_odd(7)}")
print(f"Largest of 3, 9, and 6 is: {find_largest(3, 9, 6)}")
print(f"Square of 4 is: {square(4)}")
print(f"Reverse of 'hello' is: {reverse_string('hello')}")
print(f"Area of rectangle with length 5 and width 3: {rectangle_area(5, 3)}")
