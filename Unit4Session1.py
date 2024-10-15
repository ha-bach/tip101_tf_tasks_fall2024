# PROBLEM 1
# UNDERSTAND
# 1. Share 2 questions you would ask to help understand the question:
#      What is the input of the function?
#      What is the output of the function?

# PLAN
# 2. Write out in plain English what you want to do:
#  I want to write a function that will take a number
#  and return True if its a prime number
#  and return False if it is not a prime number
#  to do that I will divide the number by everything between
#  1 and itself (both exclusive)
#  if the remainder is 0 somewhere, we return False
#  if we reach the end if no 0 remainder, we return True

# 3. Translate each sub-problem into pseudocode:
# def is_prime(n):
#  if n == 0 or n == 1 or n == 2:
#   return True
#  for num in range(2, n):
#   if n % num == 0:
#    return False
#  return True


# IMPLEMENT
def is_prime(n):
  if n == 0 or n == 1 or n == 2:
    return True
  for num in range(2, n):
    if n % num == 0:
      return False
  return True


# PROBLEM 2
# UNDERSTAND
# 1. Share 2 questions you would ask to help understand the question:
#      What is the input of the function?
#      What is the output of the function?

# PLAN
# 2. Write out in plain English what you want to do:
# 4. Translate the pseudocode into Python and share your final answer:
# I want to write a function that takes a string and reverse it in-place
# using the two pointer approach
# I can do this by having a left pointer that starts at the beginning index
# a right pointer that starts at the end index
# while the left < right pointer
#  I will swap their elements
#  and increment the pointers

# 3. Translate each sub-problem into pseudocode:
#def reverse_list(lst):
# left = 0
# right = len(lst) - 1
# while left < right:
#  lst[left], lst[right] = lst[right], lst[left]
#  left += 1
#  right -= 1
# return lst


# IMPLEMENT
# 4. Translate the pseudocode into Python and share your final answer:
def reverse_list(lst):
  left = 0
  right = len(lst) - 1
  while left < right:
    lst[left], lst[right] = lst[right], lst[left]
    left += 1
    right -= 1
  return lst


# PROBLEM 3
# UNDERSTAND
# 1. Share 2 questions you would ask to help understand the question:
#      What is space complexity?
#      What is time complexity?

# PLAN
# 2. Write out in plain English what you want to do:
# Compare space and time complexity of 2 solutions

# 3. Translate each sub-problem into pseudocode:
# No pseudocode


# IMPLEMENT
# 4. Translate the pseudocode into Python and share your final answer:
def reverse_list(lst):
  # Create a new reversed list
  reversed_lst = lst[::-1]
  # Copy the elements back into the original list
  for i in range(len(lst)):
    lst[i] = reversed_lst[i]


# Our solution is log(n) time complexity because we traverse half the input
# it has O(1) space complexity because it is reversing in-place
# This solution should be O(n) time complexity, assuming string splicing has O(n) or
# less complexity
# It create a new list, so its space complexity is O(n)

# PROBLEM 4
# UNDERSTAND
# 1. Share 2 questions you would ask to help understand the question:
#      What is the input of the function?
#      What is the output of the function?

# PLAN
# 2. Write out in plain English what you want to do:
# I will have two pointers, left at the beginning of the list and
# right and the end of the list
# In a while loop where left < right
# I will either
# increment left until it's at an odd number
# increment right until it's at an even number
# swap the two

# 3. Translate each sub-problem into pseudocode:
#def sort_array_by_parity(nums):
# left = 0
# right = len(nums) - 1
# while left < right:
#  if(nums[left] % 2 != 1):
#   ++left
#  elif(nums[right] % 2 != 0):
#   ++right
#  else:
#   nums[left], nums[right] = nums[right], nums[left]


# IMPLEMENT
# 4. Translate the pseudocode into Python and share your final answer:
def sort_array_by_parity(nums):
  left = 0
  right = len(nums) - 1
  while left < right:
    if (nums[left] % 2 != 1):
      left += 1
    elif (nums[right] % 2 != 0):
      right -= 1
    else:
      nums[left], nums[right] = nums[right], nums[left]
  return nums


# PROBLEM 5
# UNDERSTAND
# 1. Share 2 questions you would ask to help understand the question:
#      What is the input of the function?
#      What is the output of the function?

# PLAN
# 2. Write out in plain English what you want to do:
# I will write a function that takes in a list of string
# and return the first string in the list that is palindromic
# to do this I will traverse the list in order
# and check if the string is a palindrome
# if it is, I will return the string
# out of the loop, meaning no strings are palindromic
# i will return None
# i will also create a helper function that determines if the string is a palindrome
# or not
# that function takes in a string and return True or False accordingly
# i will have a pointer at the beginning (left), and a pointer at the end (right)
# while left < right, i will
#  check if left and right are the same letters
#  if they are not, i will return false
#  I will increment left and decrement right
# outside of the loop, meaning all letters matched, i will return True

# 3. Translate each sub-problem into pseudocode:
# def is_palindrome(word):
#  left = 0
#  right = len(word) - 1
#  while left < right:
#   if(nums[left] != nums[right]):
#    return False
#   left += 1
#   right -= 1
#  return True

# def first_palindrome(words):
#  for word in words:
#   if(is_palindrome(word)):
#    return word
#  return None


# IMPLEMENT
# 4. Translate the pseudocode into Python and share your final answer:
def is_palindrome(word):
 left = 0
 right = len(word) - 1
 while left < right:
  if(word[left] != word[right]):
   return False
  left += 1
  right -= 1
 return True

def first_palindrome(words):
 for word in words:
  if(is_palindrome(word)):
   return word
 return None