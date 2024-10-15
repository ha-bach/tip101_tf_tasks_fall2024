# PROBLEM 1: Long Pressed
# UNDERSTAND
# 1. Share 2 questions you would ask to help understand the question:
#      What is the input of the function?
#      What is the output of the function?

# PLAN
# 2. Write out in plain English what you want to do:
# I want to write a function that will take a name, a string and return if the
# string is a valid long-pressed name or not
# that is, if each character in their name appears at least once in the
# same order in the string
# tricky case is if two consecutive name letters are the same
# to do that, i will have a pointer i in the name
# a pointer j in the string
# and i will store a past character outside the loop
# we have to traverse to the end both the name and the string
# so while the pointers haven't reached the end
# if j is == past character
# i will increment j and continue
# i will check if i appears in j
# if not, I wil return false
# if it does, i will store i in past character
# and increment i and j
# out of the loop, i will return True

# 3. Translate each sub-problem into pseudocode:
# def is_long_pressed(name, typed):
#  i = 0
#  j = 0
#  c = None
#  while i < len(name) and j < len(typed):
#   if typed[j] == c:
#    j += 1
#    continue
#   if name[i] != typed[j]:
#    return False
#   c = name[i]
#   i += 1
#   j += 1
#  return True


# IMPLEMENT
# 4. Translate the pseudocode into Python and share your final answer:
def is_long_pressed(name, typed):
   i = 0
   j = 0
   c = None
   while i < len(name) and j < len(typed):
      if typed[j] == c:
         j += 1
         continue
      if name[i] != typed[j]:
         return False
      c = name[i]
      i += 1
      j += 1
   return True


# PROBLEM 2: Sharing Cookies
# UNDERSTAND
# 1. Share 2 questions you would ask to help understand the question:
#      What is the input of the function?
#      What is the output of the function?

# PLAN
# 2. Write out in plain English what you want to do:
# I want to maximize the numbers of contented child with a given amount of cookies
# so i will have pointer i to traverse the children ist
# pointer j to traverse the cookies list
# and counter content_children to keep track of children that has been fed
# while i < len(children list) and j < len(cookie list):
#  if child[i] <= cookies[j]
#   i increment content_children
#   and increment i
#  i increment j

# 3. Translate each sub-problem into pseudocode:
# def find_content_children(s, g):
#  i = 0
#  j = 0
#  content_children = 0
#  while i < len(g) and j < len(s):
#   if g[i] <= s[j]:
#    content_children += 1
#    i += 1
#  j += 1
#  return content_children


# IMPLEMENT
# 4. Translate the pseudocode into Python and share your final answer:
def find_content_children(s, g):
   i = 0
   j = 0
   content_children = 0
   while i < len(g) and j < len(s):
      if g[i] <= s[j]:
         content_children += 1
         i += 1
      j += 1
   return content_children


# PROBLEM 3: Valid Palindrome
# UNDERSTAND
# 1. Share 2 questions you would ask to help understand the question:
#      What is the input of the function?
#      What is the output of the function?

# PLAN
# 2. Write out in plain English what you want to do:
# I want to write a function that will return whether an input string is
# a palindrome, with at most one character removed
# To do this
# I can write a helper function, is_palindrome, that determines if a string
# is a palindrome or not
# the function will then act a normal palindrome check
# except when it fails the first time it will test 2 strings
# and see if they are palindromes
# string 1 is the og string removed the left char
# string 2 is the og string removed right char
# or, it can be recursive, with a counter

# 3. Translate each sub-problem into pseudocode:
# def valid_palindrome(s):
#  return is_valid_palindrome(1, s)

# def is_valid_palindrome(n, s):
#  if(n < 0) return False;
#  left = 0
#  right = len(s) - 1
#  while left < right:
#   if s[left] != s[right]:
#    return(n - 1, s[left:right + 1]) 
#   left += 1
#   right -= 1
#  return True

# IMPLEMENT
# 4. Translate the pseudocode into Python and share your final answer:
def valid_palindrome(s):
 return is_valid_palindrome(1, s)

def is_valid_palindrome(n, s):
 if(n < 0): 
   return False;
 left = 0
 right = len(s) - 1
 while left < right:
  if s[left] != s[right]:
   return is_valid_palindrome(n - 1, s[left:right]) or is_valid_palindrome(n - 1, s[left + 1:right + 1])
  left += 1
  right -= 1
 return True
   

# PROBLEM 4: Positive Negative Pairs
# UNDERSTAND
# 1. Share 2 questions you would ask to help understand the question:
#      What is the input of the function?
#      What is the output of the function?

# PLAN
# 2. Write out in plain English what you want to do:
# Given the input of a list of numbers, I want to find the largest matching pair
# of negative and positive numbers
# I will sort the list with two pointers
# I will a left pointer at the beginning and right pointer at the end of the list
# I will sum up the two pointers.
# If the sum is positive, I'm too far right, I decrement my right pointer
# Similarly, if sum is negative, I increment my left pointer
# If sum is 0, i return left pointer
# I do this until left meets right, and return -1

# 3. Translate each sub-problem into pseudocode:
# def find_largest_k(nums):
#  nums.sort()
#  left = 0
#  right = len(nums) - 1
#  while left < right:
#   sum = nums[left] + nums[right]
#   if sum > 0:
#    --right
#   elif sum < 0:
#    ++left
#   else:
#    return nums[left]
#  return -1

# IMPLEMENT
# 4. Translate the pseudocode into Python and share your final answer:
def find_largest_k(nums):
 nums.sort()
 left = 0
 right = len(nums) - 1
 while left < right:
  sum = nums[left] + nums[right]
  if sum > 0:
   right -= 1
  elif sum < 0:
   left += 1
  else:
   return nums[right]
 return -1


# PROBLEM 5: Good Substring
# UNDERSTAND
# 1. Share 2 questions you would ask to help understand the question:
#      What is the input of the function?
#      What is the output of the function?

# PLAN
# 2. Write out in plain English what you want to do:
# I will write a function that takes in a string and returns the number of
# substrings that it has that has exactly 3 non-repeating characters
# Two do that i will create a window of 3 characters using two pointers
# I initialize left pointer at the start of the string
# right pointer 3 indices away
# and counter for good substring
# I will run a while loop until the right pointer reaches the end of the string
#  i check the substring if it is good
#  if it is a good substring,
#   i will increment the counter
# I will make a helper function to determine a good substring
# def is_good(s: str):
#  return s[0] != s[1] and s[1] != s[2] and s[0] != s[2] 

# 3. Translate each sub-problem into pseudocode:
# def is_good(s):
#  return s[0] != s[1] and s[1] != s[2] and s[0] != s[2] 
# def count_good_substrings(s):
#  good_substrings = 0
#  left = 0
#  right = 2
#  while right < len(s):
#   if is_good(s[left:right + 1]):
#    good_substrings += 1
#  return good_substrings

# IMPLEMENT
# 4. Translate the pseudocode into Python and share your final answer:
def is_good(s):
   return s[0] != s[1] and s[1] != s[2] and s[0] != s[2] 

def count_good_substrings(s):
   good_substrings = 0
   left = 0
   right = 2
   while right < len(s):
    substr = s[left:right + 1]
    if is_good(substr):
     good_substrings += 1
    left += 1
    right += 1
   return good_substrings