"""
A set is an unordered collection with unique elements. It is optimized for fast membership testing (O(1)).

Characteristics
No duplicates.
Unordered.
Mutable.
"""

"""

Operations

Operation	    Code	Description
Add	            s.add(value)	Insert new value
Remove	        s.remove(value)	Remove, raises error if not found
Discard	        s.discard(value)	Remove, does nothing if not found
Pop	            s.pop()	Remove and return an arbitrary element
Union	        `s1	| s2`
Intersection	s1 & s2	Common elements
Difference	    s1 - s2	Elements in s1 but not in s2
Subset	        s1 <= s2	Check if s1 is a subset of s2
Superset	    s1 >= s2	Check if s1 is a superset of s2
"""
# Using curly braces
unique_ids = {101, 102, 103, 104}

# Using set() constructor
empty_set = set()  # Must use set(), {} creates a dictionary


# Set operations
A = {1, 2, 3}
B = {3, 4, 5}

# Add item into set s.add(value)
A.add(4)
A.add(7)
B.add(6)
B.add(7)

#Remove item from the set s.remove(value)
B.remove(7)

#Discard - Remove, does nothing if not found s.discard(value)
A.remove(7)

# Pop - remove and return an arbitrary element
print(unique_ids.pop())

#Union S1 | S2
print(A | B)  # Union {1, 2, 3, 4, 5, 6}

#Intersection S1 & S2
print(A & B)  # Intersection {3, 4}

#Difference S1 - S2
print(A - B)  # Difference {1, 2}

#Subset s1 <=2 Check if s1 is a subset of s2
print(A <= B)

# Superset s1 >= s2 check is s1 is a superset of s2
print(A >= B)