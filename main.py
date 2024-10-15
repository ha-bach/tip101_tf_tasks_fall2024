# PROBLEM 1
# UNDERSTAND
# 1. Share 2 questions you would ask to help understand the question:
#      What is the input of the function?
#      What is the output of the function?

# PLAN
# 2. Write out in plain English what you want to do:

# 3. Translate each sub-problem into pseudocode: 

# IMPLEMENT
# 4. Translate the pseudocode into Python and share your final answer:


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


# UPI TEMPLATE

# UNDERSTAND
# 1. Share 2 questions you would ask to help understand the question:
#      What is the input of the function?
#      What is the output of the function?

# PLAN
# 2. Write out in plain English what you want to do:

# 3. Translate each sub-problem into pseudocode: 

# IMPLEMENT
# 4. Translate the pseudocode into Python and share your final answer:


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


def print_list(node):
    current = node
    while current:
        print(current.value, end=" -> " if current.next else "")
        current = current.next
    print()


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


def main():
    head = Node(1, Node(3, Node(1, Node(4))))
    print_list(partition(head, 3))



if __name__ == "__main__":
    main()
