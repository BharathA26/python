# Type casting:
#  The typecasting is used to convert into one datatype to other 
# str(),boo(),int(),float().

print(type(123))  # Output: <class 'int'>
# 1. String to Integer
string_number = "123"
integer_number = int(string_number)
print(integer_number)  # Output: 123
# 2. Integer to String
integer_number = 456
string_number= str(integer_number)
print(string_number)  # Output: "456"
# 3. String to Float
Float_number = 3.14
string_number = str(Float_number)
print(string_number)  # Output: "3.14"
# 4. Float to String
Float_number = 3.14
string_number = str(Float_number)
print(string_number)  # Output: "3.14"
# 5. Integer to Float
integer_number = 789
float_number = float(integer_number)        
print(float_number)  # Output: 789.0
# 6. Float to Integer
float_number = 3.99
integer_number = int(float_number)      
print(integer_number)  # Output: 3
# 7. Boolean to String  
boolean_value = True    
string_value = str(boolean_value)
print(string_value)  # Output: "True"
# 8. String to Boolean
string_value = "False"
boolean_value = bool(string_value)  # Non-empty string is True
print(boolean_value)  # Output: True

