## 23/03/2025
## Functions:: Revisited

# Add two numbers
def add_two(first_number: int , second_number: int) -> int | float:
    """performs the summations of two ints or floats"""
    # function body
    result = first_number + second_number
    return result

# sub_two: by Ing MegaBoy
def sub_two (num1 , num2):
    '''
    This function takes two arguments and returns the sum of the two arguments
    '''
    return num1 - num2

r = sub_two(10, 5)
print(r)

def say_hello(name: str="stephanie") -> str:
    """say hello name"""
    return "Hello " + name

r = add_two(first_number=30, second_number=50) # 80
r1 = add_two(first_number=70, second_number=20) # 90
r3 = add_two(first_number="123", second_number="675")
print(r)
print(r1)
print("r3 = ",r3)

c = say_hello()
print(c)

def add_infinity(*numbers: int):
    return sum(numbers)

h = add_infinity(1,2,3,4,5,67,8,9)
print(h)

# closures...
# nested functions
def outer_function() -> function:
    def inner_function() -> function:
        def inner_inner_function() -> function:
            def innermost_function() -> str:
                return "Hi, I am the inner most function"
            return innermost_function
        return inner_inner_function
    return inner_function

out = outer_function()()()()
print(out)

