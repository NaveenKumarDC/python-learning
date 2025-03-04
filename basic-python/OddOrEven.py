#Function to check if a number is odd or even
def is_even(num):
    return num % 2 == 0

#Driver code
number = 4
if is_even(number):
    print(f"{number} is Even")
else:
    print(f"{number} is Odd")

# Create a list of squares for numbers 0-9
#List Comprehension
squares = [x**2 for x in range(10)]
print(squares)





