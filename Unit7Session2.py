# PROBLEM 1: Neatly Nested
# UNDERSTAND
# 1. Share 2 questions you would ask to help understand the question:
#      What is the input of the function?
#      What is the output of the function?

# PLAN
# 2. Write out in plain English what you want to do:
# I will write a recursive function that takes in a string of parentheses
# and return if they are all correctly nested
# to do this I will check the end and begin parentheses to see if they match
# if they don't i return false
# if they do i return True and if the inside is also nested
# my base case is () or an empty string

# 3. Translate each sub-problem into pseudocode:
# def is_nested(paren_s):
#   if paren_s == "()" or paren_s == "":
#       return True
#   if len(paren_s) <= 2:
#       return False
#   return paren_s[0] == "(" and paren_s[-1] == ")" and is_nested(paren_s[1:-1])

# IMPLEMENT
# 4. Translate the pseudocode into Python and share your final answer:
def is_nested(paren_s):
    if paren_s == "()" or paren_s == "":
        return True
    if len(paren_s) <= 2:
        return False
    return paren_s[0] == "(" and paren_s[-1] == ")" and is_nested(paren_s[1:-1])


# PROBLEM 2: How Many 1s
# UNDERSTAND
# 1. Share 2 questions you would ask to help understand the question:
#      What is the input of the function?
#      What is the output of the function?

# PLAN
# 2. Write out in plain English what you want to do:
# I will search for the first 1 in the array using binary search
# if i find the first 1, since everything that follows will be a 1,
# i can subtract list length to first 1 index to find out
# the number of ones
# I will find first 1 index using binary search
# So i have the left pointer pointing to the beginning of the array
# and the right pointer pointing to the last index of the array
# while left hasn't met right pointer
# i check the middle pointer to see if it is the first one index
# if it is 1, i check if the number before that is 1
# if it is not, meaning that is the first one index,
# i return list length - middle index
# if it is, meaning that the index contains a 1 but not the first,
# i've gone too far right and i will move right pointer to left of
# middle pointer
# if mid index does not contain a 1, meaning it contains a 0,
# i'm too far left, i move left pointer to the right of mid pointer
# if we exit the list, I will return 0
# need to test for edge case all 1s and all 0s

# 3. Translate each sub-problem into pseudocode:
# def count_ones(lst):
#   if lst == []:
#       return 0
#   left = 0
#   right = len(lst) - 1
#   while left < right:
#       mid = (left + right) // 2
#       if lst[mid] == 0:
#           left = mid + 1
#       else: # lst[mid] == 1
#           if lst[mid - 1] == 0:
#               return len(lst) - mid
#           right = mid - 1
#   return 0

# IMPLEMENT
# 4. Translate the pseudocode into Python and share your final answer:
def count_ones(lst):
    if not lst:
        return 0
    left = 0
    right = len(lst) - 1
    while left < right:
        mid = (left + right) // 2
        print(left, right, mid)
        if left == right:
            return len(lst) - mid
        if lst[mid] == 0:
            left = mid + 1
        else:  # lst[mid] == 1
            if lst[mid - 1] == 0:
                return len(lst) - mid
            right = mid - 1
    if left == 0:
        return len(lst)
    elif left == len(lst) - 1:
        return 0
    else:
        return -1


# PROBLEM 3: Binary Search IV
# UNDERSTAND
# 1. Share 2 questions you would ask to help understand the question:
#      What is the input of the function?
#      What is the output of the function?

# PLAN
# 2. Write out in plain English what you want to do:
# i want to implement binary search recursively
# so binary search takes in a nums list and a target
# the idea with binary search is we want to discard half the array
# that is not relevant to our search
# so first i still check if middle index contains target
# if it does, i return index, that is my base case
# another base case is if list is empty, then i return -1
# if target is bigger than mid number, i want to only look at the right array
# so i return binary search on right half of array
# else (target is smaller than mid number, i want to look at left array)
# i return binary search on left half of array

# 3. Translate each sub-problem into pseudocode:
# def binary_search(nums, target):
#   if not nums:
#       return -1
#   mid = len(nums) // 2
#   if nums[mid] == target:
#       return mid
#   if nums[mid] < target:
#       return binary_search(nums[mid + 1:])
#   return binary_search(nums[:mid - 1])

# IMPLEMENT
# 4. Translate the pseudocode into Python and share your final answer:
def binary_search(nums, target):
    if not nums:
        return -1
    mid = len(nums) // 2
    if nums[mid] == target:
        return mid
    if nums[mid] < target:
        num = binary_search(nums[mid + 1:], target)
        return num if num != -1 else -1
    return 0 + binary_search(nums[:mid], target)


# PROBLEM 4: Count Rotations
# UNDERSTAND
# 1. Share 2 questions you would ask to help understand the question:
#      What is the input of the function?
#      What is the output of the function?

# PLAN
# 2. Write out in plain English what you want to do:
# I want to count how many times a sorted list of numbers has been rotated
# since a sorted list is always non-decreasing, if we see a decreased follow up num
# it was the start of the original list
# so i can just count until i get to a decreasing num
# edge case is we get to the end and there is no decreasing number,
# because the list has never been rotated
# in that case, if count == len(list) i will return 0

# 3. Translate each sub-problem into pseudocode:

# IMPLEMENT
# 4. Translate the pseudocode into Python and share your final answer:
def count_rotations(nums):
    if len(nums) < 2:
        return 0
    i = 1
    while i < len(nums):
        if nums[i] < nums[i - 1]:
            return i
        i += 1
    return 0


# PROBLEM 5: Merge Sort I
# UNDERSTAND
# 1. Share 2 questions you would ask to help understand the question:
#      What is the input of the function?
#      What is the output of the function?

# PLAN
# 2. Write out in plain English what you want to do:
# Given a merge function that combines two sorted list
# I want to write a merge sort function that takes in an unsorted list
# and return a sorted list
# I will do this by recursive sorting the list
# I will call merge sort on each half list
# until there is only one element left
# and then in the upper function I will merge the two lists


# 3. Translate each sub-problem into pseudocode:
# so pseudocode is something like
# def merge_sort(lst):
#   if len(lst) < 2:
#       return lst
#   mid = len(lst) // 2
#   left = merge_sort(lst[:mid])
#   right = merge_sort(lst[mid:])
#   return merge(left, right)


# IMPLEMENT
# 4. Translate the pseudocode into Python and share your final answer:
def merge_sort(lst):
    if len(lst) < 2:
        return lst
    mid = len(lst) // 2
    left = merge_sort(lst[:mid])
    right = merge_sort(lst[mid:])
    return merge(left, right)
