
switch = True

while switch:
    number1 = input("Enter number1: ")
    number2 = input("Enter number2: ")
    result = int(number1) + int(number2) 
    print(result)
    q = input("press q to end or any key to continue:")
    if(q == 'q'):
        switch = False
    