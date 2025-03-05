def countdown(n):
    while n > 0:
        yield n  # Yield the current value of n and pause the function
        n -= 2

for number in countdown(5):
    print("Countdown:", number)