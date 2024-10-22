# PROBLEM 1: Hello Hello
# UNDERSTAND
# 1. Share 2 questions you would ask to help understand the question:
#      What is the input of the function?
#      What is the output of the function?

# PLAN
# 2. Write out in plain English what you want to do:
#  Write a function that says Hello the amount of times the parameter
# was passed in
# I'll use a for loop to do it

# 3. Translate each sub-problem into pseudocode:
# def repeat_hello_iterative(n):
#  for i in range(n):
#   print("Hello")

# IMPLEMENT
# 4. Translate the pseudocode into Python and share your final answer:
def repeat_hello_iterative(n):
    for i in range(n):
        print("Hello")


# PROBLEM 2: Factorial Cases
# UNDERSTAND
# 1. Share 2 questions you would ask to help understand the question:
#      What is the input of the function?
#      What is the output of the function?

# PLAN
# 2. Write out in plain English what you want to do:
# i will write a recursive function that takes in a number
# and return the factorial of that number
# to do that the function calls itself with n * n-1 until it reaches 1

# 3. Translate each sub-problem into pseudocode:
# def factorial(n):
#  if n == 1:
#   return 1
#  return n * factorial(n - 1)


# IMPLEMENT
# 4. Translate the pseudocode into Python and share your final answer:
def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)


# PROBLEM 3: Recursive Sum
# UNDERSTAND
# 1. Share 2 questions you would ask to help understand the question:
#      What is the input of the function?
#      What is the output of the function?

# PLAN
# 2. Write out in plain English what you want to do:
# i want to write a recursive function that takes in a list of numbers
# and return their sum
# i will do this by adding the first element of the list to the function
# calling the list removed the first item
# if there is only one item in the list we return that number

# 3. Translate each sub-problem into pseudocode:
# def sum_list(lst):
#  if len(lst) == 1:
#   return lst[0]
#  return lst[0] + sum_list(lst[1])

# IMPLEMENT
# 4. Translate the pseudocode into Python and share your final answer:
def sum_list(lst):
    if len(lst) == 1:
        return lst[0]
    return lst[0] + sum_list(lst[1:])
# time complexity: O(n)
# why: we are traversing the entire list once, summing as we go
# space complexity: O(n)
# we are creating a stack everytime we call the function
# since the numbers of stack calls are linearly proportional to
# the size of input, space complexity is O(n)


# PROBLEM 4: Recursive Power of 2
# UNDERSTAND
# 1. Share 2 questions you would ask to help understand the question:
#      What is the input of the function?
#      What is the output of the function?

# PLAN
# 2. Write out in plain English what you want to do:
# I want to write a recursive function that checks if an integer is a power of two
# I will do that by return whether this number is divisible by 2 and whether
# the result of the division is divisible by 2 (by calling the function on that result)
# my base case is 2, if integer is 2 i will return false

# 3. Translate each sub-problem into pseudocode:
# def is_power_of_two(n):
#   if n == 2:
#       return True
#   return n % 2 == 0 and is_power_of_two(n/2)


# IMPLEMENT
# 4. Translate the pseudocode into Python and share your final answer:
def is_power_of_two(n):
    if n == 2 or n == 0:
        return True
    return n % 2 == 0 and is_power_of_two(n / 2)
# time complexity: O(logn)
# each time we call the function the number gets smaller by half
# space complexity: O(logn)
# we need to create a stack for every half size of input


# PROBLEM 5: Binary Search I
# UNDERSTAND
# 1. Share 2 questions you would ask to help understand the question:
#      What is the input of the function?
#      What is the output of the function?

# PLAN
# 2. Write out in plain English what you want to do:
# the plan for the function is already provided in the question. basically we look at the
# middle value each time we call the function. if it is target we return it
# if not we look in the left half or right half of array
# base case is if there is only one item left
# we return if it is target

# 3. Translate each sub-problem into pseudocode:
# def binary_search(lst, target):
# Initialize a left pointer to the 0th index in the list
# Initialize a right pointer to the last index in the list

# While left pointer is less than right pointer:
# Find the middle index of the array

# If the value at the middle index is the target value:
# Return the middle index
# Else if the value at the middle index is less than our target value:
# Update pointer(s) to only search right half of the list in next loop iteration
# Else
# Update pointer(s) to only search left half of the list in next loop iteration

# If we search whole list and haven't found target value, return -1

# IMPLEMENT
# 4. Translate the pseudocode into Python and share your final answer:
def binary_search(lst, target):
    left = 0
    right = len(lst) - 1
    while left < right:
        mid = (right + left) // 2
        if lst[mid] == target:
            return mid
        if lst[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

