my_list = [1, 5, "Ali", 9.7, True] 
my_tuple = (1, 5, "Ali", 9.7, True) 



# Lists are mutable.
print(my_list)
my_list[0] = "Zain" 
print(my_list)




#### Tuples, and Strings don't support item assignment.

# Tuples are immutable
print(my_tuple)
my_tuple[0] = "Zain" # This causes an error.
print(my_tuple)


# Similarly Strings are also immutable 
str_var = "Ali Zain"
str_var[2] = "Z"
print(str_var)