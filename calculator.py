# switch = True

# while switch:
#     number1 = input("Enter number1: ")
#     number2 = input("Enter number2: ")
#     sign = input("Enter ops: ")
#     if sign == '+': 
#       result = int(number1) + int(number2) 
#     if sign == '-': 
#       result = int(number1) - int(number2)
       
#     print(result)
#     q = input("press q to end or any key to continue:")
#     if(q == 'q'):
#         switch = False

        
switch = True

def getValue():
    number1 = int(input("Enter number1: "))
    number2 = int(input("Enter number2: "))
    sign = input("Enter ops: ")
    return [number1, number2, sign]

while switch:
    number1, number2, sign = getValue()
    if sign == '+': 
      result = number1 + number2
    if sign == '-': 
      result = number1 - number2
       
    print(result)
    q = input("press q to end or any key to continue:")
    if(q == 'q'):
        switch = False
    