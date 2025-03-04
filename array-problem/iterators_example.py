# Using an iterator explicitly
numbers = [1, 2, 3]
iterator = iter(numbers)
print("First item:", next(iterator))
print("Second item:", next(iterator))
print("Third item:", next(iterator))

def countdown(n):
    while n > 0:
        yield n  # Yield the current value of n and pause the function
        n -= 1

for number in countdown(5):
    print("Countdown:", number)
