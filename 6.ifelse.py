#  if = Do some code only if condition is true 
# else = Do something else 

age = int(input("enter your age"))

if age >= 100:
       print("your dead ")
elif age<0:
    print("your are not born")
elif age >= 18:

     print("you are now signup")
else:
    print("you ar not signup bcz you are below 18")

# example 2 
reponse = input("enter the some sample ptroduct")

if reponse == "": 
     print("you enter some products details ")
else: 
     print("product are not")

# example calculator 
operator = input("enter the operators + - / *")

num1 = float(input("enter the number" ))
num2 = float(input("enter the number" ))

if operator == '+':
     result = num1 + num2
     print(result)
elif operator == '-':
      result = num1 - num2
      print(result)
elif operator == '*':
      result = num1 * num2
      print(result)
elif operator == '/':
      result = num1 / num2
      print(result)
else:
     print(f"operator is nort found{operator}")