# PROBLEM 1: Detect Circular Linked List
# UNDERSTAND
# 1. Share 2 questions you would ask to help understand the question:
#      What is the input of the function?
#      What is the output of the function?

# PLAN
# 2. Write out in plain English what you want to do:
# I want to write a function that takes in a head pointer to a linked list
# and return whether the list is circular
# to do this i will iterate through the list
# if my current pointer is at any point the same as the head pointer
# i return True
# if we reach None, meaning we are at the end of the list and it does not cycle around
# i return False

# 3. Translate each sub-problem into pseudocode: 
# def is_circular(head):
#   cur = head
#   while cur:
#     if cur is head:
#       return True
#   return False

# IMPLEMENT
# 4. Translate the pseudocode into Python and share your final answer:
def is_circular(head):
    if head.next is None:
        return False
    cur = head.next
    while cur:
        if cur is head:
            return True
        cur = cur.next
    return False


# PROBLEM 2: Find Last Node in a Linked List Cycle
# UNDERSTAND
# 1. Share 2 questions you would ask to help understand the question:
#      What is the input of the function?
#      What is the output of the function?

# PLAN
# 2. Write out in plain English what you want to do:
# i want to traverse all nodes in list
# for each node i will traverse the list again to see if some other nodes point to it
# if i see that i will return the pointer node
# if not i will return None

# 3. Translate each sub-problem into pseudocode: 
# def find_last_node_in_cycle(head):
#  cur = head
#  while cur:
#   ptr_node = find_ptr_node(cur)
#   if ptr_node:
#    return ptr_node
#   cur = cur.next
#  return None

# def find_ptr_node(head):
#  cur = head
#  while cur:
#   if cur.next is head:
#    return cur
#   cur = cur.next
#  return None

# IMPLEMENT
# 4. Translate the pseudocode into Python and share your final answer:
def find_last_node_in_cycle(head):
    cur = head
    while cur:
        ptr_node = find_ptr_node(cur)
        if ptr_node:
            return ptr_node
        cur = cur.next
    return None


def find_ptr_node(head):
    cur = head
    while cur:
        if cur.next is head:
            return cur
        cur = cur.next
    return None


# PROBLEM 3: Partition List Around Value
# UNDERSTAND
# 1. Share 2 questions you would ask to help understand the question:
#      What is the input of the function?
#      What is the output of the function?

# PLAN
# 2. Write out in plain English what you want to do:
# edge case: value not in list
# list is empty
# i want to write a function that takes in the head of a list and
# a value that i am partitioning around
# i will make a temp head node that points to the current head
# and make the temp head the head
# i will traverse the list until cur.next is a value that is smaller than val
# in that case i will make a pointer tmp that points to that value
# i will point cur.next to tmp.next
# then i will point tmp->next to head
# head will point to tmp
# return head
# this swapping should be its own function
# so i traverse the list, and everytime i see a cur next that is bigger than val
# i will call this function, pass in cur and head, and have it swap cur.next to head
# then i return the current head


# 3. Translate each sub-problem into pseudocode:
# def move_to_head(head, node)
#  tmp = node.next
#  node.next = tmp.next
#  tmp.next = head
#  return tmp

# def partition(head, val):
#  cur = head
#  while cur:
#   if cur.next.value < val:
#    head = move_to_head(head, cur)
#   cur = cur.next
#  return head

# IMPLEMENT
# 4. Translate the pseudocode into Python and share your final answer:
def move_to_head(head, node):
    tmp = node.next
    node.next = tmp.next
    tmp.next = head
    return tmp


def partition(head, val):
    cur = head
    while cur.next:
        if cur.next.value < val:
            head = move_to_head(head, cur)
        cur = cur.next
    return head


# PROBLEM 4: Convert Binary Number in a Linked List to Integer
# UNDERSTAND
# 1. Share 2 questions you would ask to help understand the question:
#      What is the input of the function?
#      What is the output of the function?

# PLAN
# 2. Write out in plain English what you want to do:
# I will traverse the list and converts one by one the value of each node
# add it to the current sum
# and return the sum at the end

# 3. Translate each sub-problem into pseudocode:
# def binary_to_int(head):
#   cur = head
#   sum = 0
#   while cur:
#     sum = sum * 2 + cur.value
#     cur = cur.next
#   return sum

# IMPLEMENT
# 4. Translate the pseudocode into Python and share your final answer:
def binary_to_int(head):
    cur = head
    sum = 0
    while cur:
        sum = sum * 2 + cur.value
        cur = cur.next
    return sum


# PROBLEM 5: Add Two Numbers Represented by Linked Lists
# UNDERSTAND
# 1. Share 2 questions you would ask to help understand the question:
#      What is the input of the function?
#      What is the output of the function?

# PLAN
# 2. Write out in plain English what you want to do:
# I will make a helper function, extract number, to extract the decimal number
# from the binary list
# then i can call it on the two lists and return the sum of the two numbers
# as for extract number, it will
# keep track of what digit we are at
# digit starts at 0
# each time we move up a node, digit increments by 1
# we calculate the value of the digit and add it to current sum
# so the calculate for each new node is sum += cur.value * 10**digit
# i also need to convert the sum into a linked list with same format
# so i can add another function to_linked_list(num)
# while num is not 0
# i extract a digit - the ones digit
# add it to tail of the list
# return num

# 3. Translate each sub-problem into pseudocode:
# def insert_tail(lst, digit):
#  if lst is None:
#   return Node(digit)
#  cur = lst
#  while cur.next:
#   cur = cur.next
#  cur.next = Node(digit)

# def to_linked_list(num):
#  lst = None
#  while num != 0:
#   digit = num % 10
#   num //= 10
#   insert_tail(lst, digit)
#  return lst

# def get_num(head):
#  num = 0
#  digit = 0
#  cur = head
#  while cur:
#   num += cur.value * 10**digit
#   digit += 1
#  return num

# def add_two_numbers(head_a, head_b):
#  return get_num(head_a) + get_num(head_b)

# IMPLEMENT
# 4. Translate the pseudocode into Python and share your final answer:
def insert_tail(lst, digit):
    if lst is None:
        lst = Node(digit)
        return lst
    cur = lst
    while cur.next:
        cur = cur.next
    cur.next = Node(digit)
    return lst


def to_linked_list(num):
    lst = None
    while num != 0:
        digit = num % 10
        num //= 10
        lst = insert_tail(lst, digit)
    return lst


def get_num(head):
    num = 0
    digit = 0
    cur = head
    while cur:
        num += cur.value * 10 ** digit
        digit += 1
        cur = cur.next
    return num


def add_two_numbers(head_a, head_b):
    return to_linked_list(get_num(head_a) + get_num(head_b))
