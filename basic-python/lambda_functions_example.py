# A lambda function that squares a number
square = lambda x: x ** 2
print("Square of 5:", square(5))

numbers = [1, 2, 3, 4]
squares = list(map(lambda x: x ** 2, numbers))
print("Squares using map:", squares)


# Get even numbers from the list
evens = list(filter(lambda x: x % 2 == 0, numbers))
print("Even numbers using filter:", evens)
