#succesfully merged




# python function to take an input number and check if it is a prime number
def prime_num():
    num=int(input("Enter a number:"))
    if num%2==0:
        print("the number is prime")
    else:
        print("the number is not prime")
prime_num()

# python function to reverse a string
def reverse_string():
    string=input("Enter a string:")
    print(string[::-1])
reverse_string()



# # python function to check if a string is a palindrome
def palindrome():
    string=input("Enter a string:")
    if string==string[::-1]:
        print("The string is a palindrome")
    else:
        print("The string is not a palindrome")
palindrome()


# python function factorial of a number
def factorial():
    num=int(input("Enter a number:"))
    fact=1
    for i in range(1,num+1):
        fact=fact*i
    print(fact)
factorial()
