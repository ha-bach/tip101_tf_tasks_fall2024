# PROBLEM 1: Contains Duplicates
# UNDERSTAND
# 1. Share 2 questions you would ask to help understand the question:
#      What is the input of the function?
#      What is the output of the function?

# PLAN
# 2. Write out in plain English what you want to do:
# i initialize an empty set
# i traverse the list
# every time i see a number, if it is not in the set, i add it into the set
# if it is in the set, i return True
# outside of the loop, i return False

# 3. Translate each sub-problem into pseudocode:
# 1) Initialize an empty set `seen`.
# 2) Iterate through each element `num` in `nums`:
#     a) If `num` is in `seen`, return True.
#     b) Otherwise, add `num` to `seen`.
# 3) If the loop completes without finding duplicates, return False.

# IMPLEMENT
# 4. Translate the pseudocode into Python and share your final answer:
def contains_duplicate(nums):
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False


# PROBLEM 2: Remove Element
# UNDERSTAND
# 1. Share 2 questions you would ask to help understand the question:
#      What is the input of the function?
#      What is the output of the function?

# PLAN
# 2. Write out in plain English what you want to do:
# I want to make a variable k that will keep track of the elements that are not val
# i iterate through the list
# if i see number that is not val
# i put number in k to current index
# i increment k
# outside the loop, i return list up to k

# 3. Translate each sub-problem into pseudocode:
# 1) Initialize a variable `k` to 0 to keep track of the number of elements not equal to `val`.
# 2) Iterate through each element `i` in the array `nums`:
#     a) If `nums[i]` is not equal to `val`:
#         i) Overwrite `nums[k]` with `nums[i]`.
#         ii) Increment `k`.
# 3) Return `k`, which represents the number of elements not equal to `val`.

# IMPLEMENT
# 4. Translate the pseudocode into Python and share your final answer:
def remove_element(nums, val):
    k = 0
    for i in range(len(nums)):
        if nums[i] != val:
            nums[k] = nums[i]
            k += 1
    return k


# PROBLEM 3: Greatest Common Divisor of Strings
# UNDERSTAND
# 1. Share 2 questions you would ask to help understand the question:
#      What is the input of the function?
#      What is the output of the function?

# PLAN
# 2. Write out in plain English what you want to do:
# i calculate the GCD of the lengths of the two strings using the Euclidean algorithm.
# i check if the prefix of the length equal to the GCD of the two string lengths can divide both str1 and str2
# If both strings are divisible by prefix,
# return the prefix as the GCD of the strings; otherwise, return an empty string.

# 3. Translate each sub-problem into pseudocode:
# 1) Define a helper function `is_divisible(s, t)` that checks if string `t` divides string `s`.
# 2) Find the GCD of the lengths of `str1` and `str2`.
# 3) Use the GCD length to extract a candidate substring from `str1`.
# 4) Check if this candidate substring divides both `str1` and `str2`.
# 5) Return the candidate substring if it divides both strings; otherwise, return an empty string.

# IMPLEMENT
# 4. Translate the pseudocode into Python and share your final answer:
def gcd_of_strings(str1, str2):
    def is_divisible(s, t):
        if len(s) % len(t) != 0:
            return False
        repeat = len(s) // len(t)
        return t * repeat == s

    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a

    gcd_length = gcd(len(str1), len(str2))
    candidate = str1[:gcd_length]

    if is_divisible(str1, candidate) and is_divisible(str2, candidate):
        return candidate
    return ""


# PROBLEM 4
# UNDERSTAND
# 1. Share 2 questions you would ask to help understand the question:
#      What is the input of the function?
#      What is the output of the function?

# PLAN
# 2. Write out in plain English what you want to do:
# i define a helper function, check_balance_and_height(node), to check if a node is balanced and calculate its height.
# if the node is None i return True (balanced) and height 0. i recursively check the left and right subtrees for balance and height,
# then determine if the current node is balanced by comparing their heights.
# i compute the current node's height and return its balance status and height.
# In the main function i call the helper function starting from the root and return whether the tree is balanced.

# 3. Translate each sub-problem into pseudocode:
# 1) Define a helper function `check_balance_and_height(node)` to check balance and calculate height.
#     a) If the current node is None, return True (balanced) and height 0.
#     b) Recursively check the left subtree for balance and height.
#     c) Recursively check the right subtree for balance and height.
#     d) Check if the current node is balanced by comparing the heights of the left and right subtrees.
#     e) Calculate the height of the current node.
#     f) Return if the current node is balanced and its height.
# 2) In the main function `is_balanced(root)`, call the helper function to start the check from the root node.
# 3) Return if the tree is balanced.

# IMPLEMENT
# 4. Translate the pseudocode into Python and share your final answer:
def check_balance_and_height(node):
    if not node:
        return True, 0

    left_balanced, left_height = check_balance_and_height(node.left)
    right_balanced, right_height = check_balance_and_height(node.right)

    balanced = left_balanced and right_balanced and abs(left_height - right_height) <= 1
    height = max(left_height, right_height) + 1

    return balanced, height

def is_balanced(root):
    balanced, height = check_balance_and_height(root)
    return balanced


# PROBLEM 5: Subarray Sum Equals K
# UNDERSTAND
# 1. Share 2 questions you would ask to help understand the question:
#      What is the input of the function?
#      What is the output of the function?

# PLAN
# 2. Write out in plain English what you want to do:
# i start with a hash map cumulative_sum to track the frequency of sums,
# initializing it with 0 mapped to 1 (for the sum 0).
# i set current_sum and count to 0. as i go through each number num in the array nums,
# i add num to current_sum. if current_sum equals k, i increase count.
# if current_sum - k is in cumulative_sum, i add its frequency to count.
# i update cumulative_sum with the new current_sum. at the end, i return count.
# 3. Translate each sub-problem into pseudocode:
# 1) Initialize a hash map `cumulative_sum` with a default value of 0 for the cumulative sum 0.
# 2) Initialize `current_sum` to 0 and `count` to 0.
# 3) Iterate through each element `num` in the array `nums`:
#     a) Add `num` to `current_sum`.
#     b) If `current_sum` is equal to `k`, increment `count`.
#     c) If `current_sum - k` exists in `cumulative_sum`, add its frequency to `count`.
#     d) Update `cumulative_sum` with `current_sum`.
# 4) Return `count`.

# IMPLEMENT
# 4. Translate the pseudocode into Python and share your final answer:
def subarray_sum(nums, k):
    cumulative_sum = {0: 1}
    current_sum = 0
    count = 0

    for num in nums:
        current_sum += num

        if current_sum == k:
            count += 1

        if current_sum - k in cumulative_sum:
            count += cumulative_sum[current_sum - k]

        if current_sum in cumulative_sum:
            cumulative_sum[current_sum] += 1
        else:
            cumulative_sum[current_sum] = 1

    return count