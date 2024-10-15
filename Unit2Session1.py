# PROBLEM 1
# UNDERSTAND
# 1. Share 2 questions you would ask to help understand the question:
#      What is the input of the function?
#      What is the output of the function?

# PLAN
# 2. Write out in plain English what you want to do:
#    I want to create a Python function that will determine if a list is a subsequence
#         of another list
#    I will have one pointer pointing at the desired subsequence, and one pointer at the
#    the list we are checking for
#    I will iterate through the list to look for the current value of my subsequence
#    pointer. When I find the value I am looking for, I will move the subsequence 
#    pointer forward to look for the next value. If my pointer reaches the end of the
#    subsequence, this means I have found a subsequence within my list, so I return true
#    If I reach the end of the list without reaching the end of the subsequence, that
#    my subsequence is not in the list, so I return false

# 3. Translate each sub-problem into pseudocode: 
#    function is_subsequence(lst, subsequence):
#        lst_idx = 0
#        sub_idx = 0
#        lst_len = length(lst)
#        sub_len = length(subsequence)
#        while true:
#          if lst[lst_idx] == subsequence[sub_idx]:
#              sub_idx += 1
#              if sub_idx == sub_len:
#                  return true
#          lst_idx += 1
#          if lst_idx == lst_len:
#              return false


# IMPLEMENT
# 4. Translate the pseudocode into Python and share your final answer:
def is_subsequence(lst, subsequence):
    lst_idx = 0
    sub_idx = 0
    lst_len = len(lst)
    sub_len = len(subsequence)
    while True:
      if sub_idx == sub_len:
        return True
      if lst_idx == lst_len:
        return False
      if lst[lst_idx] == subsequence[sub_idx]:
        sub_idx += 1
      lst_idx += 1
# better to separate checking for condition logic and incrementing logic
      
# PROBLEM 2
# UNDERSTAND
# 1. Share 2 questions you would ask to help understand the question:
#    What is the input?
#    What is the expected output?

# PLAN
# 2. Write out in plain English what you want to do:
#    I want to make a dictionary out of two lists  

# 3. Translate each sub-problem into pseudocode: 
#    function create_dictionary(keys, values):
#      result = {}
#      for i in range(len(keys)):
#        result[keys[i]] = values[i]

# IMPLEMENT
# 4. Translate the pseudocode into Python and share your final answer:
def create_dictionary(keys, values):
  result = {}
  for i in range(len(keys)):
    result[keys[i]] = values[i]
  return result

# PROBLEM 3
# UNDERSTAND
# 1. Share 2 questions you would ask to help understand the question:
#      What is the input of the function?
#      What is the output of the function?

# PLAN
# 2. Write out in plain English what you want to do:
#    I will write a function that will take in a dictionary and a key value. I will look
#    up the key value in the dictionary. If it exists, I will print the key and the 
#    value. If it does not, I will print "That pair does not exist!"

# 3. Translate each sub-problem into pseudocode: 
#  def print_pair(dictionary, target):
#    value = dictionary[target]
#    if value == None:
#      print("That pair does not exist!")
#    else:
#      print("Key: ", target)
#      print("Value ", value)
  

# IMPLEMENT
# 4. Translate the pseudocode into Python and share your final answer:
def print_pair(dictionary, target):
   if target in dictionary:
     print("Key: ", target)
     print("Value ", dictionary[target])
   else:
     print("That pair does not exist!")

# PROBLEM 4
# UNDERSTAND
# 1. Share 2 questions you would ask to help understand the question:
     #      What is the input of the function?
     #      What is the output of the function?
     
# PLAN
# 2. Write out in plain English what you want to do:
     # I will sum up the values of keys, sum up the values of values, and then compare
     # them and print out appropriate outputs

# 3. Translate each sub-problem into pseudocode: 
# def keys_v_values(dictionary):
#  k_sum = sum of keys
#  v_sum = sum of values
#  if k_sum > v_sum:
#   print("keys")
#  elif k_sum == v_sum:
#   print("values")
#  else:
#   print("balanced")

# IMPLEMENT
# 4. Translate the pseudocode into Python and share your final answer:
def keys_v_values(dictionary):
 k_sum = sum(dictionary.keys())
 v_sum = sum(dictionary.values())
 if k_sum > v_sum:
  return "keys"
 elif k_sum == v_sum:
  return "balanced"
 else:
  return "values"


