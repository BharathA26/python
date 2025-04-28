# logical operators = the evelvate the conditions (or , and and not )
# or = at least one condion is true 
# and = at all conditon is true 
# not = at the conditpn is not a number or not equal to 


temp = 5 
is_sunny = False

if temp <= 1 and is_sunny: 
    print("it is sunny")
else:
    print("it is not sunny")

if temp <= 1 or is_sunny: 
    print("it is sunny")
else:
    print("it is not sunny")

if temp <= 1 and not is_sunny: 
    print("it is sunny")
else:
    print("it is not sunny")