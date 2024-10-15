# PROBLEM 1
# UNDERSTAND
# 1. Share 2 questions you would ask to help understand the question:
#      What is the function doing?
#      How does changing the parameter change the function?

# PLAN
# 2. Write out in plain English what you want to do:
# Call the function once so that "mississipi" will be printed 5 times

# 3. Translate each sub-problem into pseudocode: 
# Call the function once
# Have "mississipi" print 5 times

# IMPLEMENT
# 4. Translate the pseudocode into Python and share your final answer:
def count_mississippi(limit):
  for num in range(1, limit):
   print( f"{num} mississippi")

count_mississippi(6)


# PROBLEM 2
# UNDERSTAND
# 1. Share 2 questions you would ask to help understand the question:
#      What is the input of the function?
#      What is the output of the function?

# PLAN
# 2. Write out in plain English what you want to do:
#  I will write a function that takes in a string
#  I will have one pointer at the start of the string
#  one pointer at the end of the string
#  Then I will create a new string that swaps the start and the end
#  of the input string
#  and return the new string
# 3. Translate each sub-problem into pseudocode: 
# def swap_ends(my_str):
#  new_str = my_str[-1] + my_str[1:-2] + my_str[0]
#  return new_str

# IMPLEMENT
# 4. Translate the pseudocode into Python and share your final answer:
def swap_ends(my_str):
 new_str = new_str = my_str[-1] + my_str[1:-1] + my_str[0]
 return new_str


# PROBLEM 3
# UNDERSTAND
# 1. Share 2 questions you would ask to help understand the question:
#      What is the input of the function?
#      What is the output of the function?

# PLAN
# 2. Write out in plain English what you want to do:
#  I want to write a function that will take a string
#  and determine if it contains every letter in the English alphabet
#  First i will create a reference table for all English letters
#  Then I will convert the string into lower case
#  I will iterate through the string and check the reference table for english 
#  characters
#  if at the end i have enough english characters (sum the reference table)
#  i will return True
#  if not, I will return False
#  I can also check for enough english letter every time i check off a new character
#  more inefficient for small strings, more efficient for large strings

# 3. Translate each sub-problem into pseudocode: 
# def is_pangram(my_str):
#  alphabet = [0] * 26
#  my_str = my_str.lower()
#  for c in my_str:
#   i = ord[c] - ord['a']
#   if alphabet[i] == 0:
#    alphabet[i] = 1
#  return sum(alphabet) == 26


# IMPLEMENT
# 4. Translate the pseudocode into Python and share your final answer:
def is_pangram(my_str):
 alphabet = [0] * 26
 my_str = my_str.lower()
 for c in my_str:
  if not c.isalpha():
    continue
  i = ord(c) - ord('a')
  if alphabet[i] == 0:
   alphabet[i] = 1
 return sum(alphabet) == 26
  

# PROBLEM 4
# UNDERSTAND
# 1. Share 2 questions you would ask to help understand the question:
#      What is the input of the function?
#      What is the output of the function?

# PLAN
# 2. Write out in plain English what you want to do:
#  I will write a function that takes in a string and returns a reverse string.
#  To do this I will write a for loop that inversely traverses the string and 
#  add the characters to the new string

# 3. Translate each sub-problem into pseudocode: 
# def reverse_string(my_str):
#  result = ""
#  for i in range(my_str - 1, -1, -1):
#   result += my_str[i]
#  return result

# IMPLEMENT
# 4. Translate the pseudocode into Python and share your final answer:
def reverse_string(my_str):
 result = ""
 for i in range(len(my_str) - 1, -1, -1):
  result += my_str[i]
 return result

