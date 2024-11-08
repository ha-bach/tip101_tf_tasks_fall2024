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


# PROBLEM 2: Root-to-Leaf Paths
# UNDERSTAND
# 1. Share 2 questions you would ask to help understand the question:
#      What is the input of the function?
#      What is the output of the function?

# PLAN
# 2. Write out in plain English what you want to do:
# Understanding
# Input: root node of a binary tree
# Output: a list containing all the possible paths to a leaf node represented by strings
# Constraint: ?
# Edge case: empty tree (list with empty string?), tree with only root (list with one string containing one value)

# Plan
# it's going to be a recursive function
# first we make a string of the current node value
# if its leaf node is "node_val"
# else its "node_val->"
# make a list call result
# then if left child
# we add string + recursive call to left child
# and add that to result
# if right child
# add string + recursive call to right child
# and add that to result
# we return result

# 3. Translate each sub-problem into pseudocode:
# def binary_tree_paths(root):
#   val = ""
#   if root:
#       val += str(root.val)
#   if root.left or root.child:
#       val += "->"

#   if root.left:
#       left_paths = binary_tree_paths(root.left)  # we get back a list of strings
#       for path in left_paths:
#           path = val + path
#   if root.right:
#       right_paths = binary_tree_paths(root.right)
#       for path in right_paths:
#           path = val + path
#   return left_paths + right_paths

# IMPLEMENT
# 4. Translate the pseudocode into Python and share your final answer:
def binary_tree_paths(root):
    if not root:
        return []

    val = ""
    if root.val:
        val += str(root.val)
    if root.left or root.right:
        val += "->"

    if not root.left and not root.right:
        return [val]

    left_paths = []
    right_paths = []
    if root.left:
        left_paths = binary_tree_paths(root.left)  # we get back a list of strings
        for i in range(len(left_paths)):
            left_paths[i] = val + left_paths[i]
    if root.right:
        right_paths = binary_tree_paths(root.right)
        for i in range(len(right_paths)):
            right_paths[i] = val + right_paths[i]
    return left_paths + right_paths

# Time complexity: O(n)
# Why: we visit every node in the tree
# Space complexity: O(n)
# Why: function is recursive, we call a stack frame for every node we visit


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