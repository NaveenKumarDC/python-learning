#Longest Increasing Subsequence (LIS)
# Given an array arr[] of size n, the task is to find the length of the Longest Increasing Subsequence (LIS)
# i.e., the longest possible subsequence in which the elements of the subsequence are sorted in increasing order.
#
# Examples:
#
# Input: arr[] = [3, 10, 2, 1, 20]
# Output: 3
# Explanation: The longest increasing subsequence is 3, 10, 20 and max sum is 33
#
# Input: arr[] = [30, 20, 10]
# Output:1
# Explanation: The longest increasing subsequences are [30], [20] and [10] and max sum is 60
#
#
# Input: arr[] = [2, 2, 2]
# Output: 1
# Explanation:  We consider only strictly increasing. and max sum is 1
#
#
# Input: arr[] = [10, 20, 35, 80]
# Output: 4
# Explanation: The whole array is sorted and max sum is 145


# Python program to find Largest increasing subsequence count using recursion
# in Exponential Time and Linear Space - Time complexity is O( 2^N) exponential
def lisEndingAtIndex(idx, array):
    #Base case
    if idx == 0:
        return 1
    #Consider all elements on the lef of i, recursively compute LISs ending with them and consider the largest
    mx = 1
    for prev in range(idx):
        if array[prev] < array[idx]:
            mx = max(mx, lisEndingAtIndex(prev, array) + 1)
    return mx

def maxLis(array):
    n = len(array)
    res = 1
    for idx in range(n):
        res = max(res, lisEndingAtIndex(idx, array))
    return res

def maxLisSumUsingMemo(idx, array, memo):
    # If value is computed return it
    if memo[idx] != -1:
        return memo[idx]

    ans = array[idx]
    #Compute values for all j in range (0, idx -1)
    for j in range(idx-1, -1, -1):
        if(array[j] < array[idx]):
            ans = max(ans, array[idx] + maxLisSumUsingMemo(j, array, memo))
    #Assign the max value at idx
    memo[idx] = ans
    return ans

def maxLisSumUsingMemoizatino(array):
    n = len(array)
    memo = [-1] * n
    ans = 0
    for idx in range(n):
        ans = max(ans, maxLisSumUsingMemo(idx, array, memo))
    return ans

#Memoization to reduce time complexity O(N^2)

# #Problem:
# Find the length of the Longest Increasing Subsequence (LIS) using Dynamic Programming (O(N²) solution).
#
# Solution Explanation
# We use a DP array (dp), where:
#
# dp[i] stores the length of LIS ending at index i.
# We iterate backwards from i-1 to 0 (using for j in range(i - 1, -1, -1)) to check all previous elements.
def lengthOfLISUsingTabulation(nums):
    if not nums:
        return 0
    n = len(nums)
    dp = [1] * n # Each element itself is a subsequence of length 1

    for i in range(1, n): #Traverse from left to right
        for j in range(i -1, -1, -1): # Check all previous elements (backward loop)
            if nums[j] < nums[i]: # Can nums[j] be include in LIS before nums[i] ?
                dp[i] = max(dp[i], dp[j] + 1) # update dp[i] to max LIS length

    return max(dp) # Return max LIS length from the dp array

# DP solution works fine but can be optimized using Binary Search + Patience Sorting to achieve O(N log N) time complexity.
# How Does the O(N log N) Approach Work?
# We maintain an increasing subsequence list (sub).
# For each number in the array:
# If it is larger than the last element in sub, append it.
# If it is smaller, replace the first element that is greater than or equal to it (using Binary Search).
# The size of sub at the end gives the length of LIS.
def lengthOfLISUsingBisect(nums):
    from bisect import bisect_left
    sub = [] # List to store the smallest possible LIS at each length
    for num in nums:
        idx = bisect_left(sub, num)

        if idx == len(sub):
            sub.append(num)  # Append if num is greater than all elements
        else:
            sub[idx] = num # Replace the first element >= num
    return len(sub)


if __name__ == "__main__":
    array = [10, 20, 35, 80, 1]
    # #O(2^n) time complexity and o(n) space
    #print(f"Number of elements in largest increasing subsequence : {maxLis(array)}")

    #O(n^2) time complexity and O(n) space
    #print(f"Memoization : Sum of all elements in largest increasing subsequence : {maxLisSumUsingMemoizatino(array)}")

    #O(n^2) time complexity and O(n) space using tabulation
    # print(f"Tabulation : Number of elements in largest increasing subsequence : {lengthOfLISUsingTabulation(array)}")

    #O(N long N)
    print(f"bisect_left : Number of elements in largest increasing subsequence : {lengthOfLISUsingBisect(array)}")