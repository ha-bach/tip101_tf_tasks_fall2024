# PROBLEM 1: Is Symmetric Tree
# UNDERSTAND
# 1. Share 2 questions you would ask to help understand the question:
#      What is the input of the function?
#      What is the output of the function?

# PLAN
# 2. Write out in plain English what you want to do:
# Understanding
# input: root node of a tree
# output: boolean indicating whether tree is symmetric
# constraints: the tree is a binary tree. any min or max height for input?
# edge case: empty tree, one node tree

# 1) If both left and right nodes are None, return True.
# 2) If only one of the nodes is None, return False.
# 3) If the values of the left and right nodes do not match, return False.
# 4) Recursively compare the left child of the left node with the right child of the right node, and the right child of the left node with the left child of the right node.
# 5) Return the result of the recursive comparisons.

# 3. Translate each sub-problem into pseudocode:
# def is_symmetric_tree(left, right):
#   if not left and not right:
#       return True
#   if not left or not right:
#       return False
#   if left.key != right.key:
#       return False
#   left = is_symmetric_tree(left.left, right.right)
#   right = is_symmetric_tree(left.right, right.left)
#   return left and right

# def is_symmetric(root):
#   if not root:
#       return True
#   return is_symmetric_tree(root.left, root.right)

# IMPLEMENT
# 4. Translate the pseudocode into Python and share your final answer:
def is_symmetric_tree(left, right):
    if not left and not right:
        return True
    if not left or not right:
        return False
    if left.val != right.val:
        return False
    left_tree = is_symmetric_tree(left.left, right.right)
    right_tree = is_symmetric_tree(left.right, right.left)
    return left_tree and right_tree


def is_symmetric(root):
    if not root:
        return True
    return is_symmetric_tree(root.left, root.right)

# Time complexity: O(n)
# Why: we are traversing every node to make sure the tree is symmetrical
# Time complexity: O(n)
# Why: We create a stack frame for every node we visit

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