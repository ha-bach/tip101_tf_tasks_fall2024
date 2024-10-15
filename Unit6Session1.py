# PROBLEM 1: Nested Constructors
# UNDERSTAND
# 1. Share 2 questions you would ask to help understand the question:
#      What is the input of the function?
#      What is the output of the function?

# PLAN
# 2. Write out in plain English what you want to do:
# I want to use the node constructor so that i can create a linked list of
# 3 elements within one Python statement

# 3. Translate each sub-problem into pseudocode: 
# call the node constructor within a node constructor within a node constructor

# IMPLEMENT
# 4. Translate the pseudocode into Python and share your final answer:
head = Node(4, Node(3, Node(2)))


# PROBLEM 2: Find Frequency
# UNDERSTAND
# 1. Share 2 questions you would ask to help understand the question:
#      What is the input of the function?
#      What is the output of the function?

# PLAN
# 2. Write out in plain English what you want to do:
# I want to write a function that takes in the head of a linked list and an
# integer value val
# I will return how many times val occurs in the linked list
# To do this i will make a variable count = 0
# i will traverse through the linked list
# everytime i see this value i will increment count
# after traversing the list i will return count

# 3. Translate each sub-problem into pseudocode: 
# def count_element(head, val):
#   count = 0
#   cur = head
#   while cur is not None:
#     if cur.value == val:
#       count += 1
#     cur = cur.next
#   return count

# IMPLEMENT
# 4. Translate the pseudocode into Python and share your final answer:
def count_element(head, val):
  count = 0
  cur = head
  while cur is not None:
    if cur.value == val:
      count += 1
    cur = cur.next
  return count
# this solution has a time complexity of O(n) and a space complexity of O(1)
# time complexity is O(n) because it needs to traverse the whole input once
# to count the occurence of val
# space complexity is O(1) because we only need to have a set amount of variables
# to keep track of the counting, we don't need more storage for bigger input sizes
  

# PROBLEM 3: Remove Tail
# UNDERSTAND
# 1. Share 2 questions you would ask to help understand the question:
#      What is the input of the function?
#      What is the output of the function?

# PLAN
# 2. Write out in plain English what you want to do:
# I want to debug the code provided 

# 3. Translate each sub-problem into pseudocode: 
# i will run the program and use print statements and stack trace to debug

# IMPLEMENT
# 4. Translate the pseudocode into Python and share your final answer:
def remove_tail(head):
  if head is None: # If the list is empty, return None
      return None
  if head.next is None: # If there's only one node, removing it leaves the list empty
      return None 

# Start from the head and find the second-to-last node
  current = head
  while current.next.next: 
      current = current.next

  current.next = None # Remove the last node by setting second-to-last node to None
  return head
# this is the fixed version. the buggy version stopped at the last node
# not the second to last node


# PROBLEM 4: Find the Middle
# UNDERSTAND
# 1. Share 2 questions you would ask to help understand the question:
#      What is the input of the function?
#      What is the output of the function?

# PLAN
# 2. Write out in plain English what you want to do:
# I want to write a function that takes in the head of a linked list
# and return the middle value
# if there are two middle values, we return the second value
# and we should try to use a fast and slow pointer with this too
# so to tackle this problem, i will
# traverse the list with two pointers, fast and slow
# slow will traverse one node at a time
# and the fast pointer will traverse two nodes at a time
# faster pointer go first
# if the fast pointer reaches the end of the list, we return where the
# slow pointer is

# 3. Translate each sub-problem into pseudocode: 
# def find_middle_element(head):
#   fast = head
#   slow = head
#   while fast:
#     fast = fast.next
#     if fast:
#       fast = fast.next
#     slow = slow.next
#   return slow.value

# IMPLEMENT
# 4. Translate the pseudocode into Python and share your final answer:
def find_middle_element(head):
  fast = head.next
  slow = head

  if not slow:
    return None

  if not fast:
    return slow

  while fast:
    fast = fast.next
    if fast:
      fast = fast.next
    slow = slow.next
  return slow.value
# time complexity: O(n)
# why: we have to traverse list once
# space complexity: O(1)
# why: only use a set amount of variable to keep track of list

# PROBLEM 5: Is Palindrome?
# UNDERSTAND
# 1. Share 2 questions you would ask to help understand the question:
#      What is the input of the function?
#      What is the output of the function?

# PLAN
# 2. Write out in plain English what you want to do:
# Given head of linked list, I want to return whether the list is palindromic or not
# list is singly-linked, so i cannot go backwards
# so i have a pointer left that starts at the head
# and a pointer right that should be at the tail of the list
# so i will increment left and decrement right until they meet
# to get to my right pointer i will traverse until the end of the list everytime
# i will create a pointer prev_right
# if right's next is prev_right, in means we've compared that node already
# so we don't go there
# if the values inside the pointers are not the same
# i will return False
# outside the loop I will return true

# 3. Translate each sub-problem into pseudocode:
# def is_palindrome(head):
#   left = head
#   prev_right = None
#   while left is not prev_right:
#     left = left.next
#     right = left
#     while right.next is not prev_right:
#       right = right.next
#     if left.value != right.value:
#       return False
#   return True


# IMPLEMENT
# 4. Translate the pseudocode into Python and share your final answer:
def is_palindrome(head):
  left = head
  prev_right = None
  right = None
  while left is not prev_right:
    right = left
    while right.next != prev_right:
      right = right.next
    if left.value != right.value:
      return False
    if left is right:
      return True
    prev_right = right
    left = left.next
  return True
# time complexity: O(n^2)
# why: I have to traverse the list once for my left pointer
#      and for every left pointer i traverse the list once for my right pointer
# space complexity: O(1)
# why: i only have a set amount of variables to keep track of pointers