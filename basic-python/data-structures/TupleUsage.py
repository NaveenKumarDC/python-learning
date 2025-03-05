"""
Tuple (tuple)
A tuple is an ordered, immutable collection. It is faster than a list for lookups and is hashable (can be used as a dictionary key).

Characteristics
Immutable (cannot be changed after creation).
Ordered.
Can contain mixed data types.
"""

"""
When to Use Tuples?
When immutability is needed (e.g., database connection details).
As dictionary keys in caching systems.
When defining constant values (e.g., HTTP status codes).
"""

"""
 # Supported operations
 Operations
Operation	      Code	        Description
Access	        t[index]	    Get element at index
Slice	        t[start:end]	Get sub-tuple
Concatenation	t1 + t2	        Merge   tuples
Count	        t.count(value)	Count occurrences
Index	        t.index(value)	Find position
"""
# Tuple with different data types
user = ("Naveen", "Principal Engineer", 11)

# Single element tuple (comma is required)
singleton = (42,)

# Accessing elements t[index]
print(user[0])  # Output: Naveen

#Get sub tuple from start to end, here end index value is exclusive here not added to the list
# t[startIndex: endIndex] - endIndex is not included in the sub tuple
print(f"sub tuple from 0 to 1 is : {user[0:2]}") #O/p Naveen, Principle Engineer

# Merge Tuples t1 + t2
tech_stack = ("Java", "Python", "Scala")

print(f" merge two tuple result : {user + tech_stack} ")


#Count occurrence of given value in tuple t.count(value)
print(f" total occurrences of Naveen : {user.count('Naveen')}")

#index of a value in a tuple t.index(value)
print(f" index of Naveen : {user.index('Naveen')}")

"""
When to Use Tuples?
When immutability is needed (e.g., database connection details).
As dictionary keys in caching systems.
When defining constant values (e.g., HTTP status codes).
"""