name = input("enter the name")

results = len(name) # len is used to ccalculate the letter in the strings 
result = name.find("h") # it is used to find the letter which placre is here it will be start with 0 index 
result = name.rfind("h") # it is used to find the letter in reverse 
result = name.capitalize() # to change the letter to capitial letter 
result = name.upper() # to change the letter to capitial letter 
result = name.lower() # to change the letter to small letter 
result = name.replace( "-", "") # to replace the letter 

print(results,result)

# validate the user input exercise
#1. username no more then 12 characters
#2. username must not contain the spaces
#3. username must not contain the digits 

username = input("enter the name is ")

if len(username) > 12: 
    print("username no more then 12 characters")
elif not username.find(' ') == -1:
     print("username no space")
elif not username.isalpha():
    print(" not contain the digits ")
else:
    print(f"welcome{username}")

    