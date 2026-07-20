def greet(name):
    return f"hello,{name}"
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def bark(self):
        return f"{self.name} says woof!"
    
print(greet("Alice"))
