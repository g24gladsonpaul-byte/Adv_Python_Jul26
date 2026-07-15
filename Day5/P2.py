# components of closure
# 1 The Outer function
# 2 The inner function
# 3 The returned inner function

def multiplier(fator):
    def multiply(x):
        return x * fator
    return multiply

double = multiplier(2)
triple = multiplier(3)

print(double(5))  # Output: 10
print(triple(5))  # Output: 15

print(double.__closure__)  # Output: (<cell at 0x7f8b8c0c1d30: int object at 0x956e20>,)
print(triple.__closure__[0].cell_contents)  