#Immutability

#Mutable
my_list = [1, 2, 3]
my_list[0] = 10
#print(my_list)  # Output: [10, 2, 3]

#Immutable
my_tuple = (1, 2, 3)
#my_tuple[0] = 10  # This will raise an error

def pure_process(data):
    # Create a new list instead of modifying the original
    return data + (4,5,6)

original = (1,2,3)

processed = pure_process(original)

print(original)  # Output: (1, 2, 3)
print(processed)  # Output: (1, 2, 3, 4, 5, 6)

