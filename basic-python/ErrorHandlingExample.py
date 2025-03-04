try:
    # Attempt to convert a non-numeric string to an integer
    x = int("not a number")
except ValueError as e:
    print("Caught a ValueError:", e)
else:
    print("Conversion successful, value is:", x)
finally:
    print("Execution of try-except block is complete.")
