#First Class Functions

#1. Assinging a function to a variable 
def say_hello(name):
    return f"hello,{name}!"
#assigning the function to a variable
greet_function = say_hello

print(greet_function("Gladson"))
print(say_hello("Gladson"))

#2 Passing function as args
def apply_operation(func,value):
    return func(value)

def double(x):
    return x * 2
#passing different functions as arguments
print(apply_operation(double,5))

#3returning function from function
def make_multiplier(factor):
    def multiplier(x):
        return x * factor
    return multiplier

double = make_multiplier(20)
print(double(2)) 

#4 storing functions in data structures
operations = {
    'add': lambda x, y: x + y,
    'subtract': lambda x, y: x - y,
}
print(operations['add'](5, 3))  # Output: 8
print(operations['subtract'](5, 3))  # Output: 2