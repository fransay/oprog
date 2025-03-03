# data types
# primitive/fundamentals

# 1. (str) string -> "sequences of characters", "francis", "jeff", "benjamin", 'ambrose'
_str = "francis"
print(_str, type(_str)) # expect francis, <class 'str>
# 2. (int, float) integers, floating point numbers -> "int represent integers, e.g 1,2,3,45" and "float represent decimals, e.g 1.00001, 2.0,3.0"
_int = 1
print(_int, type(_int)) # expect 1, <class, int>
_float = 1.0
print(_float, type(_float)) # expect 1.0, <class, float>

# 3. bool -> True or False (0, 1)
_bool_true = True
_bool_false = False

# 4. List -> ["samuel", "kojo",]
_list = [1,2,3,4,"francis", "OK", True, {1,2,3}, {"1":"son", "2": "daughter"}]
print(_list[0]) # expect 1
print(_list[1]) # expect 2

# 5. dict -> {"1":"francis", "2": "Godwin"}
_dict = {
    "1": "benjamin",
    "2": "jeff",
    "3":"francis"
}
# calling benjamin
print(_dict["1"]) # "benjamin"
print(_dict["2"]) # "jeff"

# 6. tuple -> (1,2,3,4,5,6,7) # preserve the all objects
_tuple = (6,1,2,3,4,5,6,7)
_tuple_one_element = (1,)
print("tuple = ", _tuple)

# 7. set -> {2,3,4,3,4,3,4} # {2,3,4}
_set = {5,2,3,4,3,4,3,4}
print("set =",_set)