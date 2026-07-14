#Creating Custom Iterators
class CountDown:
    def __init__(self,start):
        self.current = start
        self.start = start
    
    def __iter__(self):
        """return the iterator object itself"""
        return self
    
    def __next__(self):
        if self.current < 1:
            raise StopIteration
        

        values = self.current
        self.current -= 1
        return values

print("countdown")
countdown = CountDown(5)
print(next(countdown))  
