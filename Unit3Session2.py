# PROBLEM 1
# UNDERSTAND
# 1. Share 2 questions you would ask to help understand the question:
#      What is the input of the function?
#      What is the output of the function?

# PLAN
# 2. Write out in plain English what you want to do:
#  I will write a function that takes a list of integer strings and return their sum.
#  I will iterate the input list
#  For each number I will translate the string into integer and then add the number
#  to the sum.
#  Then I will return that sum.

# 3. Translate each sub-problem into pseudocode:
# def sum_of_number_strings(nums):
#  sum = 0
#  for str in nums:
#   num = int(str)
#   sum += num
#  return sum


# IMPLEMENT
# 4. Translate the pseudocode into Python and share your final answer:
def sum_of_number_strings(nums):
  sum = 0
  for str in nums:
    num = int(str)
    sum += num
  return sum


# PROBLEM 3
# UNDERSTAND
# 1. Share 2 questions you would ask to help understand the question:
#      What is the input of the function?
#      What is the output of the function?

# PLAN
# 2. Write out in plain English what you want to do:
#  I will write a function that will reverse the letters in a string,
#  and only the letters
#  I will have a pointer to the beginning of the string
#  and a pointer to the end of the string
#  I will make a while loop for left <= right
#  inside the loop
#  I will either
#   increment the left pointer if it is not a character
#   decrement the right pointer if it is not a character
#   swap the characters

# 3. Translate each sub-problem into pseudocode:
# def reverse_only_letters(s):
#  result = s.split()
#  left = 0
#  right = len(result)
#  while left <= right:
#   if not result[left].isalpha():
#    ++left
#   elif not result[right].isalpha():
#    --right
#   else:
#    result[left], result[right] = result[right], result[left]
#  return result.join()


# IMPLEMENT
# 4. Translate the pseudocode into Python and share your final answer:
def reverse_only_letters(s):
  result = list(s)
  left = 0
  right = len(result) - 1
  while left <= right:
    if not result[left].isalpha():
      left += 1
    elif not result[right].isalpha():
      right -= 1
    else:
      result[left], result[right] = result[right], result[left]
      right -= 1
      left += 1
  return ''.join(result)


# PROBLEM 2
# UNDERSTAND
# 1. Share 2 questions you would ask to help understand the question:
#      What is the input of the function?
#      What is the output of the function?

# PLAN
# 2. Write out in plain English what you want to do:
# I will create a function that will remove duplicate numbers
# in a list of sorted integers (in-place)
# first I will make a while loop that keeps running until
# we are at the end of the list
# i keep track of the current unique number
# i keep track of the current index
# inside the loop
#  if the current number is different than the current unique number
#   update the current unique number
#   increment the index
#  else (the current number is not unique)
#   we remove that index

# 3. Translate each sub-problem into pseudocode:
# def remove_duplicates(nums):
# i = 0
# cur_unique = None
# while i < len(nums):
#  if nums[i] != cur_unique:
#   cur_unique = nums[i]
#   i += 1
#  else:
#   nums.pop(i)

# IMPLEMENT
# 4. Translate the pseudocode into Python and share your final answer:
def remove_duplicates(nums):
 i = 0
 cur_unique = None
 while i < len(nums):
  if nums[i] != cur_unique:
   cur_unique = nums[i]
   i += 1
  else:
   nums.pop(i)
 return nums
  

# PROBLEM 4
# UNDERSTAND
# 1. Share 2 questions you would ask to help understand the question:
#      What is the input of the function?
#      What is the output of the function?

# PLAN
# 2. Write out in plain English what you want to do:
# I will write a function that takes in a string and return the length
# of the longest uniform substring
# that is, the length of the longest sequence of repeated characters
# To do that, I will iterate over the string
# I will keep track of the current character 
# I will keep track of the current substring's length
# I will keep track of the longest substring's length
# As I iterate over the loop,
#  if the character is different than the current character, it is a new substring
#   I will compare the current substring's length with the longest substring's length
#   and update if it is longer
#   current substring's length = 1
#   current character will be the new character
#  else (the current character is the same)
#   I increment the current substring's length
 
# 3. Translate each sub-problem into pseudocode:
# def longest_uniform_substring(s):
#  if len(s) == 0:
#   return 0
#  cur_char = None
#  cur_length = 1
#  longest_length = 1
#  for i in range(len(s)):
#   if s[i] != cur_char:
#    if cur_length > longest_length:
#     longest_length = cur_length
#    cur_length = 1
#    cur_char = s[i]
#   else:
#    cur_length += 1

# IMPLEMENT
# 4. Translate the pseudocode into Python and share your final answer:
def longest_uniform_substring(s):
   if len(s) == 0:
    return 0
   cur_char = None
   cur_length = 1
   longest_length = 1
   for i in range(len(s)):
    if s[i] != cur_char:
     if cur_length > longest_length:
      longest_length = cur_length
     cur_length = 1
     cur_char = s[i]
    else:
     cur_length += 1
   return longest_length