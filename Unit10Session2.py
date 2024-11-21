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

# PROBLEM 2
# UNDERSTAND
# 1. Share 2 questions you would ask to help understand the question:
#      What is the input of the function?
#      What is the output of the function?

# PLAN
# 2. Write out in plain English what you want to do:

# 3. Translate each sub-problem into pseudocode:

# IMPLEMENT
# 4. Translate the pseudocode into Python and share your final answer:


# PROBLEM 3
# UNDERSTAND
# 1. Share 2 questions you would ask to help understand the question:
#      What is the input of the function?
#      What is the output of the function?

# PLAN
# 2. Write out in plain English what you want to do:

# 3. Translate each sub-problem into pseudocode:

# IMPLEMENT
# 4. Translate the pseudocode into Python and share your final answer:


# PROBLEM 4
# UNDERSTAND
# 1. Share 2 questions you would ask to help understand the question:
#      What is the input of the function?
#      What is the output of the function?

# PLAN
# 2. Write out in plain English what you want to do:

# 3. Translate each sub-problem into pseudocode:

# IMPLEMENT
# 4. Translate the pseudocode into Python and share your final answer:


# PROBLEM 5
# UNDERSTAND
# 1. Share 2 questions you would ask to help understand the question:
#      What is the input of the function?
#      What is the output of the function?

# PLAN
# 2. Write out in plain English what you want to do:

# 3. Translate each sub-problem into pseudocode:

# IMPLEMENT
# 4. Translate the pseudocode into Python and share your final answer:
