# PROBLEM 1
# UNDERSTAND
# 1. Share 2 questions you would ask to help understand the question:
#      What is the input of the function?
#      What is the output of the function?

# PLAN
# 2. Write out in plain English what you want to do:
#      Write a function print_list() that takes in a list lst as a parameter and prints out 
#      each item in the list.

# 3. Translate each sub-problem into pseudocode: 
#    function print_list(lst)
#      for each item in lst:
#        print item

# IMPLEMENT
# 4. Translate the pseudocode into Python and share your final answer:
def print_list(lst):
  for item in lst:
    print(item)


# PROBLEM 2
# UNDERSTAND
# 1. Share 2 questions you would ask to help understand the question:
#      What is the input of the function?
#      What is the output of the function?

# PLAN
# 2. Write out in plain English what you want to do:
    # Write a function doubled() that takes in a list of integers lst as a parameter and
    # prints each item in the list multiplied by two.
    
# 3. Translate each sub-problem into pseudocode: 
    # function doubled(lst)
    #   for each item in lst:
    #     print item * 2

# IMPLEMENT
# 4. Translate the pseudocode into Python and share your final answer:
def doubled(lst):
  for item in lst:
    print(item * 2)


# PROBLEM 3
# UNDERSTAND
# 1. Share 2 questions you would ask to help understand the question:
    #      What is the input of the function?
    #      What is the output of the function?

# PLAN
# 2. Write out in plain English what you want to do:
    # Modify the function doubled() so that instead of printing the items, it returns a
    # new list of the doubled numbers.
# 3. Translate each sub-problem into pseudocode: 
    # function doubled(lst)
    #   new_list = []
    #   for each item in lst:
    #     new_list.append(item * 2)

# IMPLEMENT
# 4. Translate the pseudocode into Python and share your final answer:
def doubled(lst):
  new_list = []
  for item in lst:
    new_list.append(item * 2)
    


# PROBLEM 4
# UNDERSTAND
# 1. Share 2 questions you would ask to help understand the question:
    #      What is the input of the function?
    #      What is the output of the function?

# PLAN
# 2. Write out in plain English what you want to do:
    # Write a function flip_sign() that takes in a list of integers lst as a parameter
    # and returns a new list where each number in the original list has been multiplied 
    # by -1.
    
# 3. Translate each sub-problem into pseudocode: 
    # function flip_sign(lst)
    #   new_list = []
    #   for each item in lst:
    #     new_list.append(item * -1)

# IMPLEMENT
# 4. Translate the pseudocode into Python and share your final answer:
def flip_sign(lst):
  new_list = []
  for item in lst:
    new_list.append(item * -1)

