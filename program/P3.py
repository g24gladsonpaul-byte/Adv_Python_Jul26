#Synta
#lambda parameter_list: expression
#lambda

add_lambda = lambda a,b:a+b
print(add_lambda(10,50))

#lambda with filter()
numbers = [1,2,3,4,5,6,7,8,9,10]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)  # Output: [2, 4, 6, 8, 10]

#lambda with map()
squared = list(map(lambda x: x ** 2, numbers))
print(squared)  # Output: [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

#lambda as a key in dictionary
student = {
    'name':'Alex',
    'age': 20,
    'grade': lambda x: f"Grade:{x}%"
}
print(student['grade'](91))