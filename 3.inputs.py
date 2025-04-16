# input();
# A function that use prompt  the user to enter data that returns as the data in string format 

input_value = input("Enter your name: ")
age = input("Enter your age: ")
# in this case the input is string
# so we need to convert it into integer 
age = int(age)
age = age +1
print(f"Hello {input_value}, you are {age} years old")
print(f"Hello {input_value}")

# example of input function
length = input("enter the length of the rectangle: ")
width = input("enter the width of the rectangle; ")

area = int(length) * int(width)
print(f"The area of the rectangle is {area}")

# example of input function 
item = input("Enter the item name: ")
quantity = float(input("Enter the quantity: "))
price =int(input("Enter the price: "))
total_price = quantity * price
print(f"The total price of {quantity} {item} is {total_price}")

#mathlip function 
noun1 = input("Enter the noun1: ")
adjective1 = input("Enter the adjective1: ")
verb1 = input("Enter the verb1: ")

print(f"The {noun1} is {adjective1} and it {verb1}")