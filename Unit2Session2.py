# PROBLEM 1
# UNDERSTAND
# 1. Share 2 questions you would ask to help understand the question:
#      What is the input of the function?
#      What is the output of the function?

# PLAN
# 2. Write out in plain English what you want to do:
# I want to write a function cast_votes that will take a dictionary of votes and
# a candidate name. If the candidate exists in the dictionary, I will increment
# their value of votes. If their name is not in, I will create a dict entry for them.

# 3. Translate each sub-problem into pseudocode:
# def cast_vote(votes, candidate):
#  if candidate in votes:
#   increment votes[candidate]
#  else:
#   votes[candidate] = 1


# IMPLEMENT
# 4. Translate the pseudocode into Python and share your final answer:
def cast_vote(votes, candidate):
  if candidate in votes:
    votes[candidate] += 1
  else:
    votes[candidate] = 1


# PROBLEM 2
# UNDERSTAND
# 1. Share 2 questions you would ask to help understand the question:
#      What is the input of the function?
#      What is the output of the function?

# PLAN
# 2. Write out in plain English what you want to do:
# I want to write a function that will take two dictionaries and return a list of common
# keys of both dictionaries

# 3. Translate each sub-problem into pseudocode:
# def common_keys(dict1, dict2):
#  d1_keys = dict1.keys()
#  d2_keys = dict2.keys()
#  to_compare = []
#  other_dict = []
#  if len(d1_keys) <= len(d2_keys):
#   to_compare = d1_keys
#   other_dict = d2_keys
#  else:
#   to_compare = d2_keys
#   other_dict = d1_keys
#  result = []
#  for key in to_compare:
#   if key in other_dict:
#    result.append(key)
#  return result


# IMPLEMENT
# 4. Translate the pseudocode into Python and share your final answer:
def common_keys(dict1, dict2):
  d1_keys = dict1.keys()
  d2_keys = dict2.keys()
  to_compare = []
  other_dict = []
  if len(d1_keys) <= len(d2_keys):
    to_compare = d1_keys
    other_dict = d2_keys
  else:
    to_compare = d2_keys
    other_dict = d1_keys
  result = []
  for key in to_compare:
    if key in other_dict:
      result.append(key)
  return result


# PROBLEM 3
# UNDERSTAND
# 1. Share 2 questions you would ask to help understand the question:
#      What is the input of the function?
#      What is the output of the function?

# PLAN
# 2. Write out in plain English what you want to do:
#  I want to write a function that takes in a dictionary of tasks, each comes
#  with a priority number. I will return the task with the highest priority,
#  breaking ties using the alphabet
#  to do this, i will iterate through tasks
#  keeping track of the highest priority number and its list of task
#  removing that entry from tasks
#  at the end returning the item from the list with the highest alphabet

# 3. Translate each sub-problem into pseudocode:
# def get_highest_priority_task(tasks):
#  task_list = []
#  highest_priority = 0
#  for task in tasks:
#   priority = tasks[task]
#   if priority > highest_priority:
#    highest_priority = priority
#    task_list = [task]
#   elif priority == highest_priority:
#    task_list.append(task)
#   task_list.sort()
#  task = task_list[0]
#  tasks.pop(task)
#  return task


# IMPLEMENT
# 4. Translate the pseudocode into Python and share your final answer:
def get_highest_priority_task(tasks):
  task_list = []
  highest_priority = 0
  for task in tasks:
    priority = tasks[task]
    if priority > highest_priority:
      highest_priority = priority
      task_list = [task]
    elif priority == highest_priority:
      task_list.append(task)
    task_list.sort()
  task = task_list[0]
  tasks.pop(task)
  return task


# PROBLEM 4
# UNDERSTAND
# 1. Share 2 questions you would ask to help understand the question:
#      What is the input of the function?
#      What is the output of the function?

# PLAN
# 2. Write out in plain English what you want to do:
#      I want to task a list of integers and return a dictionary of each 
#      unique integer and their occurences.
#      To do this, I will iterate through the integers,
#      create an entry in my dict if the interger does not exist,
#      with occurence 1
#      If the integer exist I will increment its occurence
#      And then return the dict

# 3. Translate each sub-problem into pseudocode:
# def count_occurrences(nums):
#  occurences = {}
#  for num in nums:
#   if num in occurences:
#    occurences[num] += 1
#   else:
#    occurences[num] = 1
#  return occurences

# IMPLEMENT
# 4. Translate the pseudocode into Python and share your final answer:
def count_occurrences(nums):
 occurences = {}
 for num in nums:
  if num in occurences:
   occurences[num] += 1
  else:
   occurences[num] = 1
 return occurences