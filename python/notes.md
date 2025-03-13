# Notes
Python notes from several text books.

## Scalar types
int : defines unlimited precision integers 
float: defines floating point numbers
None: defines a null value
bool: true/false values

Some basic types can be casted from one form to another, for example  
str with number representations can be casted to int and floats
```py
_str = "123"
_str_to_int = int(_str) # converts str to int of base 10
_str_to_intb3 = int(_str, 3) # converts str to int of base 3
```
and vice versa.  
strings: use `r` and `\n` for raw and newline respectively
str and the other input types have methods on them.  

## Operators
- Relational operators  
use `==, !=`  
- Comparison operators  
use `>, <, <=, >=` 
- Logical operators  
use `and, or`

## Conditional control flow
Keywords mostly used here are `if, elif, else, for, and while`
- if `condition`:
    execute body
  elif `condition`:
    execute body
  else:
    execute body 

while loop  
```py
c = 5
while c != 0:
print(c)
c -= 1
```

for loop  
```py
for x in range(1, 100,3):
    print(x)
```

## Functions
Modular units of code designed to perform specific functions, returning a value 
from a function is optional, see example below to get a much clearer and better 
understanding.
e.g.
Here, 👇 function does not return any value;  
```py
def say_hello():
  print("Hello world")
```

Here,👇 function does return a value;  
```py
def say_hello():
  return "hello world"
``` 
