#List : Lists: Ordered, mutable collections of items.
fruits = ["apple", "banana", "cherry"]
fruits.append("dates")
print("List:", fruits)
fruits.remove("banana")
fruits.remove("cherry")
print(fruits)
# Mixed type example
data = ["Apple", 1, True, False]
print("Mixed Data Type data in List: ", data)

#Tuples: Ordered, immutable collections.
coordinates = (10, 20)
print("Tuple:", coordinates)
coordinates = (10, 20, 30, 40)
print("Tuple:", coordinates)


#Dictionaries: Unordered collections of key-value pairs.
person = {"name": "Alice", "age": 30}
person["city"] = "New York"
print("city" in person) # Contains in dictionary

print("Naveen" in person)
print("Dictionary:", person)


#Sets: Unordered collections of unique items.
unique_numbers = {10, 5, 3, 3, 12, 1}
print("Set:", unique_numbers) #Set: {1, 2, 3, 4}


# Generate squares of even numbers from 0 to 9
squares = [x**2 for x in range(10) if x % 2 == 0]
print("List comprehension:", squares)


# Map numbers to their squares
squares_dict = {x: x**2 for x in range(10)}
print("Dictionary comprehension:", squares_dict)
print(f"square root if 7 is {squares_dict[7]}")


# Create a set of squares for odd numbers from 0 to 9
squares_set = {x**2 for x in range(10) if x % 2 != 0}
print("Set comprehension:", squares_set)

# Create a generator for squares of numbers from 0 to 9
squares_gen = (x**2 for x in range(10))
# Converting to list to display the values
print("Generator expression:", list(squares_gen))
