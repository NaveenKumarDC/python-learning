"""
List (list)
A list is an ordered, mutable collection.

Characteristics
Ordered.
Mutable.
Supports duplicate values.

"""

"""
When to Use Lists?
When ordering matters (e.g., execution sequence).
Storing dynamic collections of items.
Stack and queue implementations.
"""

"""
Operations Supported
Operation	        Code	                 Description
Append	        l.append(value)	            Add to end
Insert	        l.insert(index, value)	    Insert at position
Extend	        l.extend(iterable)      	Merge lists
Remove	        l.remove(value)	            Remove first occurrence
Pop	            l.po p(index)	            Remove & return element
Sort	        l.sort()	                Sort elements
Reverse	        l.reverse()	                Reverse list
Index	        l.index(value)	            Get index of value
Count	        l.count(value)	            Count occurrences
"""


"""
Examples
"""
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

# Append operations : Add to end
fruits.append("Mango")
print("Updated Date of List: ", fruits)

#Insert Operation : Insert at position
fruits.insert(0, "Watermelon")
print("Updated Date of List at 0 index: ", fruits)

#Extend - Merge two Lists
fruits.extend(data)
print("Merge Fruits and Data ", fruits)

#Remove : remove first occurrence
fruits.append("Watermelon") # Add duplicate Watermelon at ende
fruits.remove("Watermelon") # Remove first occurrence of removed value
print("Removed Watermelon from List: ", fruits)

#Pop : Remove and return element at index position
print(" Fruits Popped element at index 1 : " , fruits.pop(1))

#Sort : Sort elements in natural order
#fruits.sort() # Sort will not work with Mixed types
fruits_sorted = ["mango","apple", "banana", "cherry", "apricot"]
fruits_sorted.sort()
print("Fruits sorted list :", fruits_sorted)

# Reverse the list
fruits_sorted.reverse()
print(f"Fruits reversed list {fruits_sorted}")

# get the index value of a given value
print(f"index of banana is {fruits_sorted.index("banana")}")

# count of occurrence of a given value
print(f"count of occurrences of apple : {fruits_sorted.count("apple")}")