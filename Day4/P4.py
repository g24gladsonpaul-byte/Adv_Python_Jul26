#Function Composition
def add_two(x):
    return x + 2

def subtract_five(x):
    return x - 5

def compose_functions(value):
    result = add_two(value)
    result = subtract_five(result)
    return result

#Composition using Helper function
def compose(*functions):
    def composed(result):
        for func in functions:
            result = func(result)
        return result
    return composed

#Create a Pipeline of functions
pipeline = compose(add_two, subtract_five)
print(pipeline(10))  # Output: 7