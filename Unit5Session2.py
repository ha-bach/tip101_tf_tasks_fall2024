# PROBLEM 1: Battle Pokemon
# UNDERSTAND
# 1. Share 2 questions you would ask to help understand the question:
#      What is the input of the function?
#      What is the output of the function?

# PLAN
# 2. Write out in plain English what you want to do:
# I want to write a function attack that takes the parameter opponent, who is a pokemon.
# I will decrease the opponent's hp attribute by self pokemon's damage attribute
# if the opponent does not have any hp left i will print that opponent has fainted
# else i will print the amount of damage done

# 3. Translate each sub-problem into pseudocode: 
# def attack(self, opponent):
#  opponent.hp -= self.damage
#  if opponent.hp <= 0:
#   print("<Opponent name> fainted.")
#  else:
#   print("<Pokemon name> dealt <damage> damage to <opponent name>")

# IMPLEMENT
# 4. Translate the pseudocode into Python and share your final answer:
def attack(self, opponent):
   opponent.hp -= self.damage
   if opponent.hp <= 0:
    print(opponent.name, "fainted.")
   else:
    print(self.name ,"dealt", self.damage, "damage to", \
          opponent.name)
     

# PROBLEM 2: Convert to Linked List
# UNDERSTAND
# 1. Share 2 questions you would ask to help understand the question:
#      What is the input of the function?
#      What is the output of the function?

# PLAN
# 2. Write out in plain English what you want to do:
# Given a node class, I want to create linked list of the input list.
# To do that, I will create two nodes with values from the input list and linked
# them via the next variable
# I will create a node whose value is Jigglypuff, and whose next
# is another node with the value Wigglytuff

# 3. Translate each sub-problem into pseudocode: 
# ["Jigglypuff", "Wigglytuff"]
# node_1 = Node("Jigglypuff")
# node_2 = Node("Wigglytuff")
# node_1.next = node_2

# IMPLEMENT
# 4. Translate the pseudocode into Python and share your final answer:
node_1 = Node("Jigglypuff")
node_2 = Node("Wigglytuff")
node_1.next = node_2


# PROBLEM 3: Add First
# UNDERSTAND
# 1. Share 2 questions you would ask to help understand the question:
#      What is the input of the function?
#      What is the output of the function?

# PLAN
# 2. Write out in plain English what you want to do:
# I want to write a function that will insert in the head of a linked list
# the function takes two parameters, the linked list and the node
# i want to insert
# to do this i will
# have the node's next point to current head of linked list
# have the head of the linked list point to the input node

# 3. Translate each sub-problem into pseudocode: 
# def add_first(head, new_node):
#  new_node.next = head
#  head = new_node

# IMPLEMENT
# 4. Translate the pseudocode into Python and share your final answer:
def add_first(head, new_node):
   new_node.next = head
   head = new_node
   return head
   

# PROBLEM 4: Get Tail
# UNDERSTAND
# 1. Share 2 questions you would ask to help understand the question:
#      What is the input of the function?
#      What is the output of the function?

# PLAN
# 2. Write out in plain English what you want to do:
# given the head node of a linked list, i want to return the tail node
# to do this i will
# if the head node is empty (which means the linked list is empty)
# i will then traverse the linked list until i get to the last element
# (whose next is empty)
# i will then return that last element

# 3. Translate each sub-problem into pseudocode: 
# def get_tail(head):
#  if head == None:
#    return None
#  cur == head
#  while cur.next != None:
#   cur = cur.next
#  return cur

# IMPLEMENT
# 4. Translate the pseudocode into Python and share your final answer:
def get_tail(head):
 if head is None:
   return None
 cur = head
 while cur.next is not None:
  cur = cur.next
 return cur.value
   

# PROBLEM 5: Replace Node
# UNDERSTAND
# 1. Share 2 questions you would ask to help understand the question:
#      What is the input of the function?
#      What is the output of the function?

# PLAN
# 2. Write out in plain English what you want to do:
# i will write a function that takes a head node, an original value, and
# a replacement value
# i will return the same linked list (aka head node)
# with all original values replaced by the replacement value
# to do this i will traverse the linked list until there is no more node
#  if the value of the current node is the original value
#   i will replace the value of that node with the replacement value
# i will return the original linked list (head)

# 3. Translate each sub-problem into pseudocode:
# def ll_replace(head, original, replacement):
#   cur = head
#   while cur is not None:
#     if cur.value == original:
#       cur.value = replacement
#   return head

# IMPLEMENT
# 4. Translate the pseudocode into Python and share your final answer:
def ll_replace(head, original, replacement):
  cur = head
  while cur is not None:
    if cur.value == original:
      cur.value = replacement
    cur = cur.next
  return head