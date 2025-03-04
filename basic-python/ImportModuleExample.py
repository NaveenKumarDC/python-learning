# Using import:
# Imports the entire module.

import math
print("Square root of 16 is:", math.sqrt(16))

# Using from ... import ...:
# 	Imports specific attributes or functions.
from math import pi
print("Value of pi:", pi)
print("Value of pi:", math.pi)

#Useful for shortening module names.
import numpy as np
array = np.array([1, 2, 3])
print("Numpy array:", array)


# main.py
from my_module import greet
print(greet("Alice"))
