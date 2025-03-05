# python-learning
Learn Basics of python and Data Structure and algorithms

What are we going to learn ?
## Basics of python
## Data Structures
## Algorithms
## Building Web application


## What is Python ?

Python is a high-level, interpreted, dynamically-typed, and general-purpose programming language known for its simplicity, 
readability, and versatility. It supports multiple programming paradigms, including object-oriented, functional, and procedural programming.

### Key Features of Python
* Easy to Read & Write – Python's syntax is clean and similar to English.
* Interpreted Language – No need for compilation; Python executes line by line.
* Dynamically Typed – You don't have to declare variable types.
* Garbage Collection – Python automatically manages memory.
* Extensive Standard Library – Includes modules for networking, databases, data processing, and more.
* Cross-Platform – Runs on Windows, macOS, Linux, and more.
* Huge Ecosystem – Popular libraries like NumPy, Pandas, TensorFlow, Django, Flask, and FastAPI.
* Multi-Paradigm – Supports procedural, functional, and object-oriented programming.

### Python in Enterprise Applications
Python is widely used in enterprise software due to its scalability and rich ecosystem. Some common use cases include:

1. Web Development: Django, Flask, FastAPI
2. Data Science & Machine Learning: Pandas, NumPy, TensorFlow, Scikit-Learn
3. Automation & Scripting: Automating tasks with Python scripts
4. Database Interactions: PostgreSQL, MongoDB, Redis with SQLAlchemy or PyMongo
5. Cloud & DevOps: AWS, Azure SDKs, Infrastructure automation (Ansible, Terraform)
6. Microservices & APIs: FastAPI, Flask for backend services
7. Big Data Processing: PySpark for distributed computing

### Basics of python hands-on

#### Data structures Example

##### List 
`Reference implementation example basic-python/data-structures/ListUsage.py`

List (list)
A list is an ordered, mutable collection.

Characteristics
Ordered.
Mutable.
Supports duplicate values.

When to Use Lists?
When ordering matters (e.g., execution sequence).
Storing dynamic collections of items.
Stack and queue implementations.

###### Supported operations

* Operation	        Code	                 Description
* Append	       ` l.append(value)	      `      Add to end
* Insert	       ` l.insert(index, value)`	    Insert at position
* Extend	       ` l.extend(iterable)    `  	Merge lists
* Remove	       ` l.remove(value)	      `      Remove first occurrence
* Pop	           ` l.po p(index)	      `      Remove & return element
* Sort	       ` l.sort()	          `      Sort elements
* Reverse	       ` l.reverse()	          `      Reverse list
* Index	       ` l.index(value)	      `      Get index of value
* Count	       ` l.count(value)	      `      Count occurrences

##### Sets 

`Reference implementation example basic-python/data-structures/SetsUsage.py`

A set is an unordered collection with unique elements. It is optimized for fast membership testing (O(1)).

Characteristics
No duplicates.
Unordered.
Mutable.

###### Supported operations

Operation	        Code	                  Description
* Add	            `s.add(value)	 `      Insert new value
* Remove	        `s.remove(value)	 `      Remove,  raises error if not found
* Discard	        `s.discard(value)`	   Remove, does nothing if not found
* Pop	            `s.pop()	         `      Remove and return an arbitrary element
* Union	            `s1	| s2         `      Union of s1 and s2
* Intersection	    `s1 & s2	         `      Common elements
* Difference	    `s1 - s2	         `      Elements in s1 but not in s2
* Subset	        `s1 <= s2	     `      Check if s1 is a subset of s2
* Superset	        `s1 >= s2	     `      Check if s1 is a superset of s2

##### Dictionary 
`Reference implementation example basic-python/data-structures/SetsUsage.py`

Dictionary (dict)
A dictionary in Python is an unordered, mutable collection that stores key-value pairs. It provides O(1) average-time complexity for lookups.

Characteristics
Stores data in key-value pairs.
Keys must be immutable (e.g., strings, numbers, tuples with immutable elements).
Values can be any data type.
Fast lookups (compared to lists) due to hashing.

When to Use Dictionary?
Fast lookups in enterprise applications (e.g., caching, configurations).
When data has unique keys (e.g., user profiles, API responses).
Building JSON-like structures.

###### Supported operations

* Operation	            Code	               Description
* Access	         `   d[key]	           `     Get value by key
* Add/Update	     `   d[key] =          `     value	Modify or add new key-value pair
* Delete	         `   del d[key]	       `     Remove key
* Get with Default	 `d.get(key, default)  `     Get value, return default if not found
* Keys	             `d.keys()	           `     Get all keys
* Values	         `   d.values()	       `     Get all values
* Items	             `   d.items()	       `     Get all key-value pairs
* Check Key	         `   "key" in d	       `     Check if key exists
* Looping	         `   for k, v in d.items():` Iterate over dictionary


##### Tuple
`Reference implementation example basic-python/data-structures/TupleUsage.py`
Tuple (tuple)
A tuple is an ordered, immutable collection. It is faster than a list for lookups and is hashable (can be used as a dictionary key).

Characteristics
Immutable (cannot be changed after creation).
Ordered.
Can contain mixed data types.

When to Use Tuples?
When immutability is needed (e.g., database connection details).
As dictionary keys in caching systems.
When defining constant values (e.g., HTTP status codes).

###### Supported operations

* Operation	      Code	        Description
* Access	   ` t[index]	   ` Get element at index
* Slice	       ` t[start:end]`	Get sub-tuple
* Concatenation`	t1 + t2	       ` Merge   tuples
* Count	       ` t.count(value)`	Count occurrences
* Index	       ` t.index(value)`	Find position

    Refer basic pythong package
    - Error handling try-catch
    - Data Structure Usage
    - File Operations Read/Write
    - Error Handling
    - Lamda Functions
    

## Array Problems
    All Array related problems

## pandas module examples


### TODO 

## Generators
    ### Yield
## Decorators

## SUPER Methods

## WITH

## Inheritance : Oops

## PASS statement

## Zip function 

## Range

## MAP

## Reverse

## OS Modules

## Iterator

## Random module

## Dictionary

## FORMAT

## Regular Expression RE module

## Enumerator

## Time Module 

## Pickle module - Provides options to convert to byte streams

## Static Word

## SQL lite

## Set and Frozen set

## Recursion

## Context Manager

## Flatten list

## Algorithms

## Multithreading

## Unit test and Mocking
### Pytest

### Mock
