
# for j in range(idx-1, -1, -1):
# This loop is iterating backward from idx - 1 down to 0.

# range(start, stop, step)
# start = idx - 1 → Starts at idx - 1
# stop = -1 → Stops before -1 (i.e., stops at 0)
# step = -1 → Moves backward by 1 step

idx = 5
for j in range(idx - 1, -1, -1):
    print(j)
# Output:
# Copy
# Edit
# 4
# 3
# 2
# 1
# 0

# Explanation:
#
# Starts from 4 (idx - 1)
# Moves backward: 4 → 3 → 2 → 1 → 0
# Stops before -1 (not inclusive)
# Where is this Used?
# Iterating Backwards Through a List

arr = [10, 20, 30, 40, 50]
for j in range(len(arr) - 1, -1, -1):
    print(arr[j])
# Output:
#
# Copy
# Edit
# 50
# 40
# 30
# 20
# 10
# Finding Previous Elements in a Recursion/DP Problem
#
# Useful in LIS (Longest Increasing Subsequence) where you check all previous elements before idx.
# Alternative Way to Iterate Backward
# Using Python slicing:

for j in reversed(range(idx)):
    print(f"reversed range index idx: {idx} -> {j}")

for element in reversed(arr):
    print(f"Reversed array {element}")