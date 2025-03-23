# Functions
# code resuability is much more importantly enhances modularity

# Task: checking if a number is even or odd
# Approach 1: Without a function definition
number = 6
if number % 2 == 0:
    print("Number is even")
elif number % 2 == 1:
    print("Number is odd")
else:
    print("Can't determine number type")
    
# Approach 2: With a function definition
def is_even_or_odd(number: int) -> str:
    if number % 2 == 0:
        return ("Number is even")
    elif number % 2 == 1:
        return ("Number is odd")
    return("Can't determine number type")

# Multiple function calls
a = is_even_or_odd(1)
print("a", a)
b = is_even_or_odd(2)
print("b", b)
c = is_even_or_odd(10)
print("c", c)
d = is_even_or_odd(20)
print("d", d)

# exponent2
def exponent2(number: int) -> int:
    """returns an exponent 2 of number"""
    return number * number

# exponent 3
def exponent3(number: int|float) -> int:
    """returns an exponent 3 of number"""
    return number * number * number

exp2 = exponent2(20)
print("exp2 =", exp2)

exp3 = exponent3(2.00)
print("exp3 = ", exp3)

# Nested functions && closures.
