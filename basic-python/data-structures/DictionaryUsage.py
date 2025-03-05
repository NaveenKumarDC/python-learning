"""
Dictionary (dict)
A dictionary in Python is an unordered, mutable collection that stores key-value pairs. It provides O(1) average-time complexity for lookups.

Characteristics
Stores data in key-value pairs.
Keys must be immutable (e.g., strings, numbers, tuples with immutable elements).
Values can be any data type.
Fast lookups (compared to lists) due to hashing.
"""

"""
When to Use Dictionary?
Fast lookups in enterprise applications (e.g., caching, configurations).
When data has unique keys (e.g., user profiles, API responses).
Building JSON-like structures.
"""

"""
Operations
Operation	        Code	               Description
Access	            d[key]	                Get value by key
Add/Update	        d[key] =                value	Modify or add new key-value pair
Delete	            del d[key]	            Remove key
Get with Default	d.get(key, default)     Get value, return default if not found
Keys	            d.keys()	            Get all keys
Values	            d.values()	            Get all values
Items	            d.items()	            Get all key-value pairs
Check Key	        "key" in d	            Check if key exists
Looping	            for k, v in d.items():	Iterate over dictionary
"""

# Using curly braces
employee = {
    "name": "Naveen",
    "role": "Principal Engineer",
    "company": "Gainsight"
}


# Using dict() constructor
config = dict(host="localhost", port=5432, db="postgres")

# Access key d[key]
print(employee["name"])  # Access value

# Add/Update key d[key] = value
employee["Place"] = "Bengaluru"
print(f" Employee : {employee}")

# Delete or Remove key del d[key]
del employee["Place"]
print(f" Employee : {employee}")

# Get with default value d.get(key, Default)
print(f" Employee Access value with Default value: {employee.get("place", "Bengaluru")}")


#Get all the keys d.keys()
print(f" Get all the keys in dict Employee : {employee.keys()}")

#Get all the values d.values()
print(f" Get all the values in dict Employee : {employee.values()}")

#Get all the key value pair d.items()
print(f" Get all the key value pair in dict Employee : {employee.items()}")

#Check if key exists in dict "key" in d
print(f" Key exists in dict Employee : {"name" in employee}")

#Looping for k,v in d.items()
for k, v in employee.items():
    print(f" Key : {k} : value : {v}")


# Dictionary Operations
config["timeout"] = 30  # Adding a new key
config["host"] = "127.0.0.1"  # Updating value

if "port" in config:
    print(f"Port exists: {config['port']}")

for key, value in config.items():
    print(f"{key}: {value}")

del config["db"]  # Delete key