def greetins():
    print("hello world",end=",")
    print("how are you?")
    

greetins()
greetins()

def addition(x,y=100):
    result = x + y
    print(result)
    
addition(10)
addition(12,80)

def add(x,y):
    return x + y

x = add(10,66) + add(10,6333) * 2
print(x)
